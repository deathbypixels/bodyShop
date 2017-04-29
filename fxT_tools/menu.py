# add fxT menu
sideBar = nuke.menu('Nodes')
fxT = sideBar.addMenu('fxT', icon='fxT_menu.png')

# add fxT_chromaticAberration Group to the fxT menu
fxT.addCommand('fxT_chromaticAberration', "nuke.createNode('fxT_chromaticAberration')", icon='Shuffle.png')

# add fxT_glowy Gizmo to the fxT menu
fxT.addCommand('fxT_glowy', "nuke.createNode('fxT_glowy')", icon='Glow.png')



# add fxT_disableNodes Gizmo to the fxT menu

fxT.addCommand('fxT_disableNodes', "nuke.createNode('fxT_disableNodes')", 'Alt+d', icon='fxT_disableNodes.png')



# add fxT_edgeMatte Gizmo to the fxT menu

fxT.addCommand('fxT_edgeMatte', "nuke.createNode('fxT_edgeMatte')", icon='EdgeDetect.png')

# add fxT_matteOverlay Gizmo to the fxT menu

fxT.addCommand('fxT_matteOverlay', "nuke.createNode('fxT_matteOverlay')", icon='Radial.png')

# add fxT_matteOverlay Gizmo to the fxT menu
fxT.addCommand('fxT_matteQC', "nuke.createNode('fxT_matteQC')", icon='Radial.png')

# add fxT_relinker to the fxT menu

import fxT_relinker
fxT.addCommand("fxT_relinker", "fxT_relinker.fun()", 'Alt+r', icon="fxT_relinker.png")

# add fxT_revealInFolder to the fxT menu

import fxT_revealInFolder
fxT.addCommand('fxT_reveal in folder', 'fxT_revealInFolder.open()', icon='fxT_revealInFolder.png')