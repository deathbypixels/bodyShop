import nuke

def paintFlip():
	currentX =  nuke.selectedNode()["toolbar_source_transform_translate"].value()[0]
	currentY =  nuke.selectedNode()["toolbar_source_transform_translate"].value()[1]
	nuke.selectedNode()["toolbar_source_transform_translate"].setValue((currentX*-1, currentY*-1))
