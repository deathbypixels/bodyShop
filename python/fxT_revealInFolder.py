"""======================================================================================================================
DEVELOPER: Tor Andreassen - www.fxtor.net
DATE: July 18, 2015
VERSION: v2.0

DESCRIPTION:
    This script loops through all selected nodes and checks if the node has a file knob.
    If a file knob is present, the path will be opened in the OS file manager/browser.
    The user will be notified if nothing is selected or if the user does not select any nodes that have an existing file-path.
    If a selected node has a nonexistent path, this will be printed in the script editor, and the script will continue to process
    the next selected node.

    When opening multiple file paths that all have the same folder, only one instance of the folder will be opened (to avoid opening duplicate paths).
    For write nodes, the folder will be opened as long as a directory exists. Due to rendered files being frequently opened and deleted, write nodes only test for an existing directory.
   
    OS Support: Windows, OSX, Linux

    Supports: Existing paths of the type:
        - scripted paths (for example, paths made up of TCL)
        - local paths
        - server paths

USAGE:
    copy this python file into your .nuke directory/fxT_tools/fxT_revealInFolder
    copy the icon files into your .nuke directory/icons/fxT_icons

    put this in your init.py file:
        nuke.pluginAddPath('./fxT_tools/fxT_revealInFolder')
        nuke.pluginAddPath('./icons/fxT_icons')

    put this in your menu.py file:
        # add fxT menu
        sideBar = nuke.menu('Nodes')
        fxT = sideBar.addMenu('fxT', icon='fxT_menu.png')

        # add fxT_revealInFolder to the fxT menu
        import fxT_revealInFolder
        fxT.addCommand('fxT_reveal in folder', 'fxT_revealInFolder.open()', icon='fxT_revealInFolder.png')

NOTES:
    Place these icons and python files in the suggested paths above or wherever your NUKE_PATH is located.
    If you don't have a meny.py file or an init.py file, create one and place it in your .nuke directory or wherever your NUKE_PATH is located.

    As there is no standard file manager on Linux, I have chosen to set the file manager/browser for Linux as a fixed variable.
    This can be set in the 'fxT_setLinuxFileManager.py' file, where you can also find instructions for how to set your chosen file manager.

======================================================================================================================"""

import nuke, nukescripts, os, sys, time, subprocess
import fxT_setLinuxFileManager

def fxT_revealInFolder():
    #set variables for OS platform and selected nodes
    platform = sys.platform
    selectedNodes = nuke.selectedNodes()
    linuxBrowser = fxT_setLinuxFileManager.fileManager


    #if nothing is selected: throw popup message at user and exit the function
    if not selectedNodes:
        nuke.message('Nothing is selected, no file(s) to open.')
        return 0


    # save all selected nodes with a file-knob to a list, except the Viewer-node
    hasFileKnob = []
    for i in selectedNodes:
        if 'file' in i.knobs() and not i.name().startswith('Viewer'):
            hasFileKnob.append(i)


    # if no selected node(s) has a file knob: throw popup message at user and exit the function
    if not hasFileKnob:
        nuke.message('No file(s) to open.\n\nThis tool can only open the folder of the selected node(s) if one or more file-knobs exists.')
        return 0



    #loop throgh the saved list of nodes that has file-knobs to generate the correct directory path
    for i in hasFileKnob:
        #get the evaluated path of the file knob (to ensure scripted paths will work)
        fileKnob = i.knob('file').evaluate()
        #save the original evaluated path of the file knob for later use
        originalfileKnob = fileKnob


        #testing that the the file-knob text input field is not empty
        #and that it is not a Write node; write nodes are handeled seperatly (see below)
        if fileKnob and (i.Class() != 'Write'):

            #get the directory path
            nukeDirectory = os.path.dirname(fileKnob)

            #if the directory exists, do stuff
            if os.path.isdir(nukeDirectory):

                #generating paths with OS specific seperators
                nukeFolder = nukeDirectory.split('/') #splitting on '/' since Nuke always works with forward slashes
                osFolder = ''
                
                #if user is running on Windows, generate Windows specific paths
                if platform.startswith('win'):
                    #Windows local paths:
                    if not originalfileKnob.startswith('//'):

                        winDrive = nukeFolder[0]
                        osFolder = nukeFolder[1:]
                        osFolder = os.path.join('',*osFolder)
                        osFolder = winDrive+os.sep+osFolder

                    #Windows server paths:
                    if originalfileKnob.startswith('//'):
                        osFolder = os.sep+os.path.join(os.sep, *nukeFolder)

                else:
                    #if user is not running Windows: generate Unix paths:
                    osFolder = os.path.join(os.sep, *nukeFolder)

                #get start of filename
                filenameStart = os.path.basename(originalfileKnob)
                filenameStart = filenameStart.split('.')
                filenameStart = filenameStart[0]

                #get extention of filename
                filenameEnd = os.path.basename(originalfileKnob)
                filenameEnd = filenameEnd.split('.')
                filenameEnd = filenameEnd[-1]


                #loop throw directory to get a a valid filename
                for file in os.listdir(osFolder):
                    #if filename start and ends with the same name as what is in the fileknob: grab the first filename in the directory
                    #then break out of the loop as one only need one matching filename to verify that the file exists.
                    #PS: .startswith() and .endswith() will not garantee a perfect filematch, but it gives some leeway if the filename
                    #for example is accedently changed while this tool is running, and it allows for both sequenses and singles files (it will skip padding matching).

                    #create variable to test aginst for a existing file path
                    realPath = ''
                    if file.startswith(filenameStart) and file.endswith(filenameEnd):
                        filename = file

                        if platform.startswith('win'):
                            #local path Windows
                            if not originalfileKnob.startswith('//'):
                                realPath = osFolder.encode('string-escape')+os.sep+os.sep+filename
                            #server path for Windows
                            else:
                                realPath = osFolder+os.sep+filename
                        #paths for Unix
                        else:
                            realPath = osFolder+os.sep+filename
                            #if user is opening multiple paths: wait for 0.5 seconds to not process code too fast (avoiding dropped paths on OSX):
                            #(0.3) seems to be enough wait time, but using (0.5) to make sure slower computers don't have any problems
                            if len(hasFileKnob) > 1:
                                time.sleep(0.5)
                        #break out of the loop as one only need one filename to confirm a existing path (to not loop over large sequences of files)
                        break

                #if file exists in the selected node(s): open directory path in the OS browser.
                if os.path.isfile(realPath):

                    #print what node and filepath is being opened in the script editor
                    print "'%s': Opening folder; %s" % (i.name(), osFolder)

                    #open in OS browser
                    openPath = os.path.dirname(osFolder+os.sep)

                    if platform.startswith('win') or platform == 'darwin':
                        nukescripts.start(openPath)
                        #if user is opening multiple paths: wait for 0.5 seconds to let Finder and 3rd party browsers not drop any paths due to python executing
                        #code while process is still processing. (0.3) seems to be enough wait time. However, using (0.5) to make sure slower computers don't have any problems
                        if len(hasFileKnob) > 1:
                            time.sleep(0.5)
                    
                    elif platform.startswith('linux'):
                        subprocess.Popen([linuxBrowser, openPath])
                        if len(hasFileKnob) > 1:
                            time.sleep(0.5)






                else:
                    #if the file does not exist: printing useful info in the script editor
                    displayFileDir = originalfileKnob.replace('/', os.sep)
                    print "'%s': Nonexistent file-path; %s" % (i.name(), displayFileDir)

            else:
                #if the directory does not exist: printing useful info in the script editor
                #printing the directory path of the original fileKnob with correct OS seperators
                #if the user tries to open a path that only have characters and no folders, print the raw string
                displayDir = originalfileKnob
                if '/' in displayDir:
                    displayDir = displayDir.split('/')
                    displayDir = displayDir[0:-1]
                    displayDir =  '/'.join(displayDir)
                    displayDir = displayDir.replace('/', os.sep)
                print "'%s': Nonexistent directory-path; %s" % (i.name(), displayDir)





        #Write node paths are generally frequently opened by users; files might be deleted by the user to write out new files
        #if there was an error in the render for example. Therefore allowing to open Write node fileknob paths as long as
        #the directory exist : skipping the test for an existing file path.
        if fileKnob and (i.Class() == 'Write'):
            #get the directory path
            nukeDirectory = os.path.dirname(fileKnob)

            #if the directory exists: open directory
            if os.path.isdir(nukeDirectory):

                #generating paths with OS specific seperators
                nukeFolder = nukeDirectory.split('/') #spitting on '/' since nuke always works with forward slash
                osFolder = ''
                
                #if user is running on Windows, generate Windows specific paths
                if platform.startswith('win'):

                    #Windows local paths:
                    if not originalfileKnob.startswith('//'):

                        winDrive = nukeFolder[0]
                        osFolder = nukeFolder[1:]
                        osFolder = os.path.join('',*osFolder)
                        osFolder = winDrive+os.sep+osFolder

                    #Windows server paths:
                    if originalfileKnob.startswith('//'):
                        osFolder = os.sep+os.path.join(os.sep, *nukeFolder)

                else:
                    #if user is not running Windows: generate Unix path:
                    osFolder = os.path.join(os.sep, *nukeFolder)

                #if Write node directory exists in selected node(s): open it in the OS browser.
                if os.path.isdir(osFolder):

                    #print what node and directory-path is being opened in the script editor
                    print "'%s': Opening write-node with existing directory-path; %s" % (i.name(), osFolder)

                    #open in OS browser
                    openPath = os.path.dirname(osFolder)

                    if platform.startswith('win') or platform == 'darwin':
                        nukescripts.start(openPath)
                        
                        #if user is opening multiple paths: wait for 0.5 seconds to let Finder and 3rd party browsers not drop any paths due to python executing
                        #code while process is still processing. (0.3) seems to be enough wait time. However, using (0.5) to make sure slower computers don't have any problems
                        if len(hasFileKnob) > 1:
                            time.sleep(0.5)
                    
                    elif platform.startswith('linux'):
                        print 'openPath is'+openPath
                        subprocess.Popup([linuxBrowser, openPath])
                        if len(hasFileKnob) > 1:
                            time.sleep(0.5)



            else:
                #if the directory does not exist: printing useful info in the script editor
                #printing the directory path of the original fileKnob with correct OS seperators
                #if the user tries to open a path that only have characters and no folders, print the raw string
                displayDir = originalfileKnob
                if '/' in displayDir:
                    displayDir = displayDir.split('/')
                    displayDir = displayDir[0:-1]
                    displayDir =  '/'.join(displayDir)
                    displayDir = displayDir.replace('/', os.sep)
                print "'%s': Nonexistent directory-path; %s" % (i.name(), displayDir)


        if not fileKnob:
            #if the file knob is empty (is None or ''): printing useful info in the script editor
            print "'%s': The file-knob of this node was empty. File-knob value; %s" % (i.name(), originalfileKnob)



def open():
    return fxT_revealInFolder()