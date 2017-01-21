#Copyright (c) 2014 Imagineer Systems Ltd

__author__ = 'Imagineer Systems'


import nuke
from mocha import send_to_mocha

nuke.pluginAddPath('./icons')

nuke.menu('Nodes').addCommand( 'Send Read Node to mocha', 'send_to_mocha.send_to_mocha()', icon='mochaproicon.png')