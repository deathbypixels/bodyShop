"""======================================================================================================================
DEVELOPER: Tor Andreassen - www.fxtor.net
DATE: May 23, 2016
VERSION: v1.1

DESCRIPTION:
    This script overwrites the standard FrameHold node in Nuke, with this improved FrameHold node.
    By default the 'first_frame' knob of the FrameHold will be the current frame on the timeline (in stead of the standard '0')
    There is also a tab with 2 buttons to change the frame number to go to the previous or next frame (because: why not? and who likes to type numbers maually... )

USAGE:
    copy this python file into your .nuke directory

    put this in your menu.py file:
        import FrameHold
        nuke.menu('Nodes').addCommand("Time/FrameHold", "FrameHold.newFrameHold()", icon="frameHold.png")

======================================================================================================================"""
import nuke

def newFrameHold():

    myNode = nuke.nodes.FrameHold()
    myNode['first_frame'].setValue(nuke.frame())  #set first-frame knob to be the curren frame

    if len(nuke.selectedNodes()) >= 1:
        curSel = nuke.selectedNode()
        myNode.setInput(0, curSel)
    else:
        #generate mouse pointer position by creating node and deleting it, pulling it's x and y position for later use
        tempNode = nuke.createNode('NoOp')
        xpos = tempNode.xpos()
        ypos = tempNode.ypos()
        nuke.delete(tempNode)
        #set x and y pos for node created with no selection
        myNode.setXpos(xpos)
        myNode.setYpos(ypos)

    #add custom name tab
    tab = nuke.Tab_Knob('changeFrame') # make locic name for the tab
    divider1 = nuke.Text_Knob('','') # make dividerline seperator

    #create buttons
    myNode.addKnob(tab)
    buttonPyPrev = nuke.PyScript_Knob("previous frame", "previous frame")
    buttonPyNext = nuke.PyScript_Knob("next frame", "next frame")

    #add stuff to node
    myNode.addKnob(buttonPyPrev)
    myNode.addKnob(buttonPyNext)
    myNode.addKnob(divider1)
    buttonPyPrev.setValue('FrameHold.previousFrame()')
    buttonPyNext.setValue('FrameHold.nextFrame()')

    """opening the custom holdFrame"""
    myNode.showControlPanel()


#crete the functions that executes when pushing the buttons
def previousFrame():
    # change frame to previous frame
    curr = nuke.frame()
    prev = curr-1
    nuke.frame(prev)

    #update frame node number
    nuke.thisNode()['first_frame'].setValue(prev)


def nextFrame():
    # change frame to previous frame
    curr = nuke.frame()
    nxt = curr+1
    nuke.frame(nxt)

    #update frame node number
    nuke.thisNode()['first_frame'].setValue(nxt)