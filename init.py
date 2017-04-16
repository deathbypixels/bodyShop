# Fix filepaths cross platform
import platform
def filenameFix(filename):
    if platform.system() in ("Windows", "Microsoft"):
        return filename.replace( "/Volumes/bodyshopserver/", "Z:\\" )
    return filename.replace( "Z:\\", "/Volumes/bodyshopserver/" )

# Verbose debuggimg
import callbacksTrace

# Adds the builtin rollingAutosave to save yourself from bad script saves
import nukescripts.rollingAutoSave

# Create write dirs if they don't exist
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

# region Set knob defaults
nuke.knobDefault("Read.before", "black")
nuke.knobDefault("Read.after", "black")
nuke.knobDefault("Root.first_frame", "1001")
nuke.knobDefault("Root.last_frame", "2001")
nuke.knobDefault("Viewer.viewerProcess", "rec709")
nuke.knobDefault("Root.fps", "23.976")
nuke.knobDefault("Root.format", "HD_1080")
# nuke.knobDefault( 'channels', 'rgba' )
# endregion


# region Add plugin paths
# Add the subfolders in the .nuke directory for organization
nuke.pluginAddPath( './gizmos' )
nuke.pluginAddPath( './python' )
nuke.pluginAddPath( './plugins' )
nuke.pluginAddPath( './icons')

# From Simon Jokshlies - www.leafpictures.de
nuke.pluginAddPath("default")

# Add Render Finished Message
nuke.pluginAddPath("./renderFinished")

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

# add nuke plugin path for V!Tools http://www.victorperez.co.uk/
# V!ctor Tools Folder
# Copyright (c) 2016 Victor Perez. All Rights Reserved.
nuke.pluginAddPath('./V_Tools')
# endregion


