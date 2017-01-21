"""======================================================================================================================
DEVELOPER: Tor Andreassen - www.fxtor.net
DATE: July 18, 2015
VERSION: v1.0

DESCRIPTION:
    This file is where you specify the path to the Linux file manager/browser used when opening folder and file
    locations in Nuke with the 'fxT_revealInFolder.py' script.
  
USAGE:
    copy this python file into the same folder as the 'fxT_revealInFolder.py'
 
NOTES:   
    As there is a variety of file managers to choose from on Linux systems, and not any standard file manager for all linux-distro's,
    I have chosen to set the file manager as a fixed code for Linux users.
    Below you can see that the file manager of my choice is set to Dolphin.
    To change it to your preferred file manager, just replace the below string with the path to your chosen file manager.
    I have commented out an example below that shows how it would look for the file manager 'Thunar'.

    To find the path to your installed file manager, you can open Terminal and type:
        'which' followed by the filemanager you have installed on your system.
            example1: which dolphin
            example2: which thunar
        This will output the path you need to replace in the code below.
        Please do not replace the varable name 'fileManager' (this is used in the main python file: fxT_revealInFolder.py).
======================================================================================================================"""

fileManager ='/usr/bin/dolphin'
#fileManager ='/usr/bin/thunar'