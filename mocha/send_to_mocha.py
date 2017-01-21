
# Copyright (c) 2014 Imagineer Systems Ltd
# Script: 'Send to mocha'
# Version: 1.0.0

__author__ = 'Imagineer Systems'


import nuke
import nukescripts

import platform
import subprocess
import os


class mocha_locator_dialog(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, "Choose mocha executable location", "uk.co.thefoundry.FramePanel")
        self.path = nuke.File_Knob("path", "Path:")
        self.addKnob(self.path)

    def showDialog(self):
        result = nukescripts.PythonPanel.showModalDialog(self)
        if result:
            return (self.path.value())


class send_to_mocha():


    def __init__(self):

        self.mocha_path = self.get_mocha_path()
        if self.mocha_path != 'None':
            self.load_mocha_with_clip()


    def get_mocha_path(self):

        sys = platform.system()
        if sys == 'Darwin':
            default_path = '/Applications/mocha Pro 5.app/Contents/MacOS/mochapro'

        elif sys == 'Windows':
            default_path = r'C:\Program Files\Imagineer Systems Ltd\mocha Pro V5\bin\mochapro.exe'
        else:
            default_path = '/opt/isl/mochaproV5/bin/mochapro'

        if os.path.isfile(default_path) != True:
            home = os.path.expanduser("~")
            f = open(home+'/.nuke/mocha/mochapath.txt','r+')
            xFile = f.readlines()

            if len(xFile) == 0:
                while os.path.isfile(default_path) != True:
                    default_path = str(mocha_locator_dialog().showDialog())
                    if os.path.isfile(default_path) == True:
                        f.seek(0)
                        f.write(default_path)
                        f.truncate()
                    elif default_path == 'None':
                        return default_path
                    else:
                        nuke.message('Not a valid path:'+str(default_path))
            else:
                default_path = xFile[0]

            f.close()
        return default_path


    def get_readnode(self):
        try:
            selected_node = nuke.selectedNode()
        except:
            nuke.message('Please select a read node')
            return 0

        if selected_node.Class() == 'Read':
            footage_path = nuke.filename(selected_node, nuke.REPLACE)
            return footage_path
        else:
            nuke.message('Please select a read node to send to mocha')


    def open_mocha_with_file(self,filepath):

        #Open mocha

        footage_firstframe = nuke.selectedNode().firstFrame()

        in_point = str(nuke.Root().firstFrame()-footage_firstframe)
        out_point = str(nuke.Root().lastFrame()-footage_firstframe)


        frame_rate = str(nuke.Root().fps())

        cmd = [self.mocha_path, '--in', in_point, '--out', out_point, '--frame-rate', frame_rate, filepath]

        try:
            err = subprocess.Popen(cmd) #open mocha with the project file as a separate process
        except subprocess.CalledProcessError, e:
            print "Ping stdout output:\n", e.output

        return err


    def load_mocha_with_clip(self):
        filepath = self.get_readnode()
        if filepath:
            self.open_mocha_with_file(filepath)