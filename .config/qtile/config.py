####### IMPORTS #########
import os
import subprocess

from libqtile import hook, layout

from get_keybindings import get_keybindings
from groups import CreateGroups
# Local Files
from keybindings import Mouse
from layouts import Layouts
from widgets import MyWidgets
from functions import Functions

# from typing import List  # noqa: F401


###### MAIN ######
if __name__ in ["config", "__main__"]:
    # Initializes objects
    # obj_keys = Keybindings()
    obj_mouse = Mouse()
    obj_widgets = MyWidgets()
    obj_layouts = Layouts()
    obj_groups = CreateGroups()
    # Initializes qtile variables
    keys = get_keybindings()
    mouse = obj_mouse.init_mouse()
    layouts = obj_layouts.init_layouts()
    groups = obj_groups.init_groups()

    ### DISPLAYS WIDGETS IN THE SCREEN ####

    screens = obj_widgets.init_screen()
    main_widgets_list = obj_widgets.init_widgets_list("left")
    widgets_screen1 = obj_widgets.init_widgets_list("left")

dgroups_key_binder = None
dgrups_app_rules = []
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'xephyr'},
    {'wmclass': 'Xephyr'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call((home + '/.config/qtile/autostart.sh').split())

    # Init the monitor groups
    Functions.go_to_group("L1")
    Functions.go_to_group("R1")


@hook.subscribe.startup
def start():
    # Regenerate the docs
    subprocess.call("python3 /home/steve/.config/qtile/generate_docs.py".split())


@hook.subscribe.restart
def restart():
    # Regenerate the docs
    subprocess.call("python3 /home/steve/.config/qtile/generate_docs.py".split())


@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in,
# java that happens to be on java's whitelist.
wmname = "LG3D"
