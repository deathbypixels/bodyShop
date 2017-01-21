import nuke

import default
import paintFlip
import trackerfromcard

nuke.menu("Animation").addCommand("default/set as new knobDefault", "default.createDefault()")

nuke.menu("Animation").addCommand("default/reset", "default.resetToDefault()")

##BodyShop customizations
import autowrite

#### From Nukepedia - Ben Dickson

try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()

# From Xavier Borque
import pixelfudger

## From Nukepedia - Frederick Averpil
import readFromWrite
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Read from Write', 'readFromWrite.ReadFromWrite()', 'shift+r' )

## From Nukepedia - Frederick Averpil
## Make Browse Dir function
import browseDir
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Browse/Node\'s file path', "browseDir.browseDirByNode()" )
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Browse/Scripts folder', "browseDir.browseDir('scripts')" )
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Paint/paintFlip', paintFlip.paintFlip, 'shift+f' )

# Various Edge Gizmos for Keying
# From Nukepedia - Frank Reuter
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Keying/Edge Extend', "nuke.createNode('EdgeExtend')" )

## From Nukepedia - Bertrand Lempereur
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Keying/Edge Extend 2', "nuke.createNode('EdgeExtend2')" )

## From Nukepedia - Michael Garrett
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Keying/Vector Extend Edge', "nuke.createNode('VectorExtendEdge')" )

## From Nukepedia -
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Keying/Despill Madness', "nuke.createNode('DespillMadness')" )

## From Nukepedia - Luma Pictures
nuke.menu( 'Nuke' ).addCommand( 'Utilities/Keying/Luma Grain', "nuke.createNode('L_Grain_v05')" )

# From Tor Andreassen - http://www.fxtor.net/
import FrameHold

nuke.menu('Nodes').addCommand("Time/FrameHold", "FrameHold.newFrameHold()", icon="frameHold.png")

# From Xavier Martin - www.xaviermartinvfx.com
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("X_Tools", icon="X_Tools.png")
m.addCommand("X_Denoise", "nuke.createNode ('X_Denoise')", icon="X_Denoise.png")
m.addCommand("X_Distort", "nuke.createNode ('X_Distort')", icon="X_Distort.png")
m.addCommand("X_Tesla", "nuke.createNode('X_Tesla')", icon='X_Tesla.png')


# From Adam - Card to Tracker
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Custom")

toolbar.addCommand( 'Custom/CardtoTracker', trackerfromcard.trackerFromCard )

# add nuke plugin path for W_Hotbox www.woutergilsing.com
import W_hotbox, W_hotboxManager

# V!ctor GUI Customization
# Copyright (c) 2016 Victor Perez. All Rights Reserved.

# Import V!ctor Tools Python Files
import V_PresetBackdrop
import V_PostageStampGenerator
import V_GenerateReadFromWrite
import V_ConvertGizmosToGroups

# V!ctor Tools Nuke Menu Definitions
VictorMenu = nuke.menu('Nuke').addMenu('V!ctor')
VictorMenu.addCommand('Preset Backdrop', 'V_PresetBackdrop.presetBackdrop()', 'ctrl+alt+b')
VictorMenu.addCommand('Generate PostageStamp from node', 'V_PostageStampGenerator.postageStampGenerator()', 'ctrl+alt+p')
VictorMenu.addCommand('Generate Read node from Write node', 'V_GenerateReadFromWrite.generateReadFromWrite()', 'ctrl+r')
VictorMenu.addCommand('Convert Gizmo to Group', 'V_ConvertGizmosToGroups.convertGizmosToGroups()', 'ctrl+shift+h')

# V!ctor Tools Toolbar Definitions http://www.victorperez.co.uk/
toolbar = nuke.menu('Nodes')
VMenu = toolbar.addMenu('V!ctor', icon='V_Victor.png')
VMenu.addCommand('V_CheckMatte', 'nuke.createNode("V_CheckMatte")', icon='V_CheckMatte.png')
VMenu.addCommand('V_IdBuilder', 'nuke.createNode("V_IdBuilder")', icon='V_IdBuilder.png')
VMenu.addCommand('V_IdPackage', 'nuke.createNode("V_IdPackage")', icon='V_IdPackage.png')
VMenu.addCommand('V_IdFilter', 'nuke.createNode("V_IdFilter")', icon='V_IdFilter.png')
VMenu.addCommand('V_EdgeMatte', 'nuke.createNode("V_EdgeMatte")', icon='V_EdgeMatte.png')
VMenu.addCommand('V_Multilabeler', 'nuke.createNode("V_Multilabeler")', icon='V_Multilabeler.png')
VMenu.addCommand('V_ColorRenditionChart', 'nuke.createNode("V_ColorRenditionChart")', icon='V_ColorRenditionChart.png')
VMenu.addCommand('V_CompareView', 'nuke.createNode("V_CompareView")', icon='V_CompareView.png')
VMenu.addCommand('V_SliceTool', 'nuke.createNode("V_SliceTool")',  icon='V_SliceTool.png')
VMenu.addCommand('V_Slate', 'nuke.createNode("V_Slate")', icon='V_Slate.png')
VMenu.addCommand('V_FormatUVGenerator', 'nuke.createNode("V_FormatUVGenerator")', icon='V_FormatUVGenerator.png')
VMenu.addCommand('V_BBoxToFormat', 'nuke.createNode("V_BBoxToFormat")', icon='V_BBoxToFormat.png')
VMenu.addCommand('V_TrackingCone', 'nuke.createNode("V_TrackingCone")', icon='V_TrackingCone.png')
VMenu.addCommand('V_TrackingCone3D', 'nuke.createNode("V_TrackingCone3D")', icon='V_TrackingCone3D.png')
VMenu.addCommand('V_3DAxis', 'nuke.createNode("V_3DAxis")', icon='V_3DAxis.png')
VMenu.addCommand('V_ColorCube', 'nuke.createNode("V_ColorCube")', icon='V_ColorCube.png')
VMenu.addCommand('V_ColorTracker', 'nuke.createNode("V_ColorTracker")', icon='V_ColorTracker.png')
VMenu.addCommand('V_Solarize', 'nuke.createNode("V_Solarize")', icon='V_Solarize.png')


