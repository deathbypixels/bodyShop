import nuke
import default
import default_helper as helper

default_menu = nuke.menu("Nuke").addMenu("Scripts/default")
default_menu.addCommand("defaults window", default.show_defaults_window, "", icon="")
default_menu.addSeparator()
default_menu.addCommand("about", default.show_about, icon="")

nuke.menu("Animation").addCommand("default/set as new knobDefault", "default.create_default()")
nuke.menu("Animation").addCommand("default/show knob list", "default.show_knob_list()")
nuke.menu("Animation").addCommand("default/reset", "default.reset_to_default()")

helper.load_knob_defaults(init=True)


