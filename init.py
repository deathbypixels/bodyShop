#Verbose debuggimg
import callbacksTrace

## Adds the builtin rollingAutosave to save yourself from bad script saves
#import nukescripts.rollingAutoSave

#Add the subfolders in the .nuke directory for organization
nuke.pluginAddPath( './gizmos' )
nuke.pluginAddPath( './python' )
nuke.pluginAddPath( './plugins' )
nuke.pluginAddPath( './icons')
nuke.pluginAddPath("./renderFinished")

#Add knob defaults utility from Simon Jokuschies / leaf pictures
nuke.pluginAddPath('default')

#Create write dirs if they don't exist
def createWriteDir():
  import nuke, os, errno
  file = nuke.filename(nuke.thisNode())
  dir = os.path.dirname( file )
  osdir = nuke.callbacks.filenameFilter( dir )
  # cope with the directory existing already by ignoring that exception
  try:
    os.makedirs( osdir )
  except OSError, e:
    if e.errno != errno.EEXIST:
      raise
nuke.addBeforeRender(createWriteDir)

#Set useful Node defaults or not ...
#nuke.knobDefault("Write.raw", "True")
#nuke.knobDefault("Read.raw", "True")
nuke.knobDefault("Read.before", "black")
nuke.knobDefault("Read.after", "black")
nuke.knobDefault("Root.first_frame", "101")
nuke.knobDefault("Root.last_frame", "201")
nuke.knobDefault("Viewer.viewerProcess", "rec709")

nuke.knobDefault("Root.fps", "23.976")
nuke.knobDefault("Root.format", "HD_1080")

# add nuke plugin paths for fxT tools and icons

nuke.pluginAddPath('./fxT_tools')
nuke.pluginAddPath('./icons/fxT_icons')

# add nuke plugin path for PixelFudger tools Xavier Bourque / http://www.pixelfudger.com/

nuke.pluginAddPath('pixelfudger')

# www.imagineersystems.com - Add icon & code for send to Mocha
nuke.pluginAddPath( './mocha')

# add nuke plugin path for X Tools www.xaviermartinvfx.com
nuke.pluginAddPath( './X_Tools' )
nuke.pluginAddPath( './X_Tools/Icons' )
nuke.pluginAddPath( './X_Tools/Gizmos' )

# add nuke plugin path for W_Hotbox www.woutergilsing.com

nuke.pluginAddPath('./W_Hotbox')
nuke.pluginAddPath('./W_Hotbox/icons')

### add nuke plugin path for V!Tools http://www.victorperez.co.uk/
### V!ctor Tools Folder
### Copyright (c) 2016 Victor Perez. All Rights Reserved.
nuke.pluginAddPath('./V_Tools')


