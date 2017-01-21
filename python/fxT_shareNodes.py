"""======================================================================================================================
DEVELOPER: Tor Andreassen - www.fxtor.net
DATE: July 17, 2015
VERSION: v1.3

DESCRIPTION:
    Nuke Pane (python panel) for sharing nodes between Nuke-users on the same network.
    In stead of sending an email with nodes to another Nuke User, this script will make it possible to share nodes from
    inside Nuke to other users on the same network.

    To share nodes with other users: Select the nodes you want to share, then click on the 'Send Nodes' button inside the custom Nuke Pane.
    To grab nodes other users shared: Click the 'Get Nodes' button inside the custom Nuke Pane.

    Shared nodes is saved in a .nk-script available on the server where everyone can access the script.
    Nodes shared will exist in the script till another user shares a new set of nodes.
    This node-shareing script is very much a temporary sharing spot for nodes, as all users can share and
    overwite current shared nodes. It's not meant as a way of saving nodes for later access,
    it is more a quick tool for sending nodes to fellow artists.
USAGE:
    Copy this python file into your .nuke directory/fxT_tools, or where you choose to install the tool.

    On line 60 in this script, set the path to the nukeScript that will be used to share nodes between users.
    PS: This path must be somewhere on the server so that all users can access it.
   
    put this in your menu.py file:
        import fxT_shareNodes

    make the script visable to Nuke by adding a plugin path to the init.py file (example below)
        nuke.pluginAddPath('./fxT_tools')

    To open the tool inside Nuke, just add the new pane, it will be available under 'Windows/Custom/fxT_shareNodes'
    Save a new Workspace with the tool added for easy access the next time Nuke is opened.

NOTES:
    Make sure all computers on the network has access to this script if you want to share nodes between all users.
======================================================================================================================"""
import os, nuke, nukescripts

class nukeShare(nukescripts.PythonPanel):

    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'fxT_shareNodes', 'com.fxt.fxT_shareNodes')
      
        #create buttons
        #calling this file when button is pushed by saying: fxT_shareNodes().nukeShare()
        self.sendButton = nuke.PyScript_Knob('Send','Send Nodes','fxT_shareNodes.nukeShare().send()')
        self.getButton = nuke.PyScript_Knob('Get','Get Nodes','fxT_shareNodes.nukeShare().get()')        
        
        #create divider line
        self.divline01 = nuke.Text_Knob("","","")
        self.divline02 = nuke.Text_Knob("","","")

        #create some text info for the users
        self.info = nuke.Text_Knob("","","Select the nodes you want to share, then click the send-button\n\nTo pick up the nodes, click the get-button")
        self.copyright = nuke.Text_Knob("","","<font color='#838383'>// fxT_shareNodes v1.3 &#169; Tor Andreassen - www.fxtor.net</font>")


        # Set the path below to the nukeScript that will be used to share nodes between users.
        # There is no need to create this .nk-script manually, this python script will take care of that.
        self.tempPath = '//vfx/assets/nuke/public/fxT_shareNodes/fxT_shareNodes.nk'

        #add buttons to pane
        self.addKnob(self.sendButton)
        self.addKnob(self.getButton)
        self.addKnob(self.divline01)
        self.addKnob(self.info)
        self.addKnob(self.divline02)
        self.addKnob(self.copyright)

    def resetSel(self):
        for each in nuke.allNodes():
            each.knob("selected").setValue(False)


    def send(self):
        path = self.tempPath
        sel = nuke.selectedNodes()
        nuke.nodeCopy(path)
        self.resetSel()
        print 'fxT_shareNodes; Selected nodes was just shared'

    def get(self):
        path = self.tempPath
        nuke.scriptSource(path)
        self.resetSel()
        print 'fxT_shareNodes; Currently shared nodes was just imported'


# add to pane
def addPanel():
    return nukeShare().addToPane()


menu = nuke.menu('Pane')
menu.addCommand('fxt_shareNodes', addPanel)
nukescripts.registerPanel('com.fxt.fxT_shareNodes', addPanel)