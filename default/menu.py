"""Nuke menu.py which adds all commands to nuke' ui."""

# Import third-party modules
import nuke

# Import local modules
from default import default_main
from default import helper
from default import about

# Create menu structure
default_menu = nuke.menu("Nuke").addMenu("Bodyshop/Other")
default_menu.addCommand("defaults window", default_main.show_defaults_window)
default_menu.addSeparator()
default_menu.addCommand("about", about.show_about, icon="")

# Add commands to animation menu.
nuke.menu("Animation").addCommand("default/set as new knobDefault",
                                  "default_main.create_default()")

nuke.menu("Animation").addCommand("default/show knob list",
                                  "default_main.show_knob_list()")

nuke.menu("Animation").addCommand("default/reset",
                                  "default_main.reset_to_default()")

# Auto load knob defaults when launching.
helper.load_knob_defaults(init=True)

