"""
"Trackerfromcard"

Adam Smith, 2015

Makes a 2D Nuke 7 tracker node from a selected 3D matchmoved card.
"""

import nuke

def calculateFrameRange(i):
	firstFrame = nuke.animationStart()
	lastFrame = nuke.animationEnd()
	
	frameRange = []
	f = firstFrame
	while f <=lastFrame:
		frameRange.append(f)
		f += 1
	return frameRange

def makeTracker(reconciles):
	
	reconcile = reconciles
	
	trackNode = nuke.Node("Tracker4")
	
	for x in reconcile:
		trackNode["add_track"].execute()
		
	count = 0
	for x in reconcile:
		range = calculateFrameRange(x["output"])
		trackers = trackNode["tracks"]
		for t in range:
			recX = x["output"].getValueAt(t, 0)
			recY = x['output'].getValueAt(t, 1)
			trackers.setValueAt
			nCols = 31
			xCol = 2
			yCol = 3
			trackers.setValueAt(recX, t, count*nCols + xCol)
			trackers.setValueAt(recY, t, count*nCols + yCol)
		count += 1
		
	trackNode.setInput(0,None)

def trackerFromCard():

	sel = nuke.selectedNode()
	
	barackobama = sel.dependent()
	
	if sel.Class() != "Card2" or sel == None:
		nuke.message("Please select a tracked card")
		return
		
	moveme = nuke.Node("Axis")
	moveme.setName("MOVE_ME")
	moveme['tile_color'].setValue(0x00FF00)
	
	moveme['translate'].setValue(sel['translate'].value())
	moveme['rotate'].setValue(sel['rotate'].value())
	moveme['scaling'].setValue(sel['scaling'].value())
	moveme['uniform_scale'].setValue(sel['uniform_scale'].value())
	
	ymult = 1.0 * nuke.root().format().height()/nuke.root().format().width()/nuke.root().format().pixelAspect()
	child1 = nuke.Node('Axis')
	child1.setInput(0, moveme)
	child1.knob('translate').setValue([-0.5, 0.5*ymult, 0])
	rec1 = nuke.Node("Reconcile3D")
	child2 = nuke.Node('Axis')
	child2.setInput(0, moveme)
	child2.knob('translate').setValue([0.5, 0.5*ymult, 0])
	rec2 = nuke.Node("Reconcile3D")
	child3 = nuke.Node('Axis')
	child3.setInput(0, moveme)
	child3.knob('translate').setValue([0.5, -0.5*ymult, 0])
	rec3 = nuke.Node("Reconcile3D")
	child4 = nuke.Node('Axis')
	child4.setInput(0, moveme)
	child4.knob('translate').setValue([-0.5, -0.5*ymult, 0])
	rec4 = nuke.Node("Reconcile3D")
	
	i = 0
	
	dep = sel.dependent()[i]
	
	while dep.Class() == "Viewer":
		i += 1
		dep = sel.dependent()[i]
		
	while dep.Class() != "ScanlineRender":
		if len(dep.dependent()) == 0:
			nuke.message("No Camera Found")
		dep = dep.dependent()[0]
		
	cam = dep.input(2)
	rec1.setInput(1,cam)
	rec2.setInput(1,cam)
	rec3.setInput(1,cam)
	rec4.setInput(1,cam)
	
	p=nuke.Panel ('Set range')
	_first = int(nuke.root().knob("first_frame").value())
	_last = int(nuke.root().knob("last_frame").value())
	
	p.addSingleLineInput('Start', _first)
	p.addSingleLineInput('End', _last)
	result=p.show()
	
	if result:
		fs=int(p.value('Start'))
		fe=int(p.value('End'))
	
	nuke.execute(rec1, fs, fe)
	nuke.execute(rec2, fs, fe)
	nuke.execute(rec3, fs, fe)
	nuke.execute(rec4, fs, fe)
	
	recs = [rec1, rec2, rec3, rec4]
	
	makeTracker(recs)
	
	nuke.delete(moveme)
	nuke.delete(child1)
	nuke.delete(child2)
	nuke.delete(child3)
	nuke.delete(child4)
	nuke.delete(rec1)
	nuke.delete(rec2)
	nuke.delete(rec3)
	nuke.delete(rec4)