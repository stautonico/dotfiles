from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# Import the function that move the window to the next and prev group
from functions import Functions


# from icons import group_icons

class Section:
    def __init__(self, name, description=""):
        """
        Used to generate markdown, removed before passed to QTile
        """
        self.name = name
        self.description = description


class Keybindings:
    def __init__(self):
        self.mod = "mod4"
        self.alt = "mod1"
        self.alt_right = "mod5"
        self.shift = "shift"
        self.control = "control"

    def init_keys(self):
        keys = []

        # Essential Controls #
        keys.append(Section("Essentials"))
        keys.append(Key([self.mod], "Tab", lazy.next_layout(),
                        desc="Next layout"))

        keys.append(Key([self.mod, self.shift], "Tab", lazy.prev_layout(),
                        desc="Previous layout"))

        keys.append(Key([self.mod], "w", lazy.window.kill(),
                        desc="Kill focused window"))

        keys.append(Key([self.mod, self.control], "r",
                        lazy.restart(), desc="Restart qtile"))

        keys.append(Key([self.mod, self.control], "q",
                        lazy.shutdown(), desc="Shutdown qtile"))

        # Bindings for MonadTall #
        keys.append(Section("MonadTall Layout Controls"))
        keys.append(Key([self.mod], "h", lazy.layout.left(), desc="Focus left"))
        keys.append(Key([self.mod], "l", lazy.layout.right(), desc="Focus right"))
        keys.append(Key([self.mod], "j", lazy.layout.down(), desc="Focus down"))
        keys.append(Key([self.mod], "k", lazy.layout.up(), desc="Focus up"))
        keys.append(Key([self.mod, self.shift], "h", lazy.layout.swap_left(), desc="Shift window left"))
        keys.append(Key([self.mod, self.shift], "l", lazy.layout.swap_right(), desc="Shift window right"))
        keys.append(Key([self.mod, self.shift], "j", lazy.layout.shuffle_down(), desc="Shift window down"))
        keys.append(Key([self.mod, self.shift], "k", lazy.layout.shuffle_up(), desc="Shift window up"))
        keys.append(Key([self.mod], "i", lazy.layout.grow(), desc="Make window bigger"))
        keys.append(Key([self.mod], "o", lazy.layout.shrink(), desc="Make window smaller"))
        keys.append(Key([self.mod, self.shift], "n", lazy.layout.normalize(), desc="Reset all window sizes"))
        keys.append(Key([self.mod], "Page_Up", lazy.layout.maximize(), desc="Make focused window fullscreen"))
        keys.append(Key([self.mod, self.shift], "space", lazy.layout.flip(), desc="Mirror the current layout"))

        # Bindings for Floating #
        keys.append(Section("Floating Layout Controls"))
        keys.append(Key([self.mod, "shift"], "f", lazy.window.toggle_floating(),
                        desc='toggle floating'))
        keys.append(Key([self.mod, "shift"], "g", lazy.window.toggle_fullscreen(),
                        desc='Toggle fullscreen'))

        # Move window between monitors #
        keys.append(Section("Monitor Nav Controls"))
        keys.append(Key([self.mod], "End", Functions.window_to_next_screen(),
                        desc="Move screen to the right monitor"))
        keys.append(Key([self.mod], "Home", Functions.window_to_previous_screen(),
                        desc="Move screen to the left monitor"))
        keys.append(Key([self.mod], "period", lazy.next_screen(), desc="Move focus to next screen"))
        keys.append(Key([self.mod], "comma", lazy.prev_screen(), desc="Move focus to previous screen"))

        # Change group #
        keys.append(Section("Group Controls"))
        # Mod + 1/2/3: Changes group on left monitor
        # Mod + 8/9/0: Changes group on right monitor
        for prefix in "LR":
            for char in "123":
                if prefix == "R":
                    input_button = ["8", "9", "0"][int(char) - 1]
                else:
                    input_button = ["1", "2", "3"][int(char) - 1]
                keys.append(Key([self.mod], input_button, lazy.function(Functions.go_to_group(prefix + char)),
                                desc=f"Switch to workspace {prefix + char}"))
                keys.append(Key([self.mod, self.shift], input_button, lazy.window.togroup(prefix + char),
                                desc=f"Move window to workspace {prefix + char}"))

        # Shortcut for switching to "special" groups
        # Special groups are meant for specific apps/types of apps (etc discord group)
        # Discord
        keys.append(Key([self.mod, self.control], "d", lazy.group["Discord"].toscreen(),
                        desc="Switch to the Discord group on the focused monitor."))

        # Shortcuts #
        keys.append(Section("Shortcuts"))
        keys.append(Key([self.mod], "t", lazy.spawn(
            "/usr/bin/alacritty"), desc="Launch terminal"))

        keys.append(Key([self.mod], "f", lazy.spawn("/usr/bin/firefox-developer-edition"), desc="Launch Firefox"))

        keys.append(Key([self.mod, self.shift], "e", lazy.spawn("/usr/bin/pcmanfm"), desc="Launch PCManFM"))
        keys.append(Key([self.mod], "e", lazy.spawn("/usr/bin/alacritty -e nnn"), desc="Launch NNN"))

        keys.append(Key([self.mod], "space", lazy.spawn('custom_rofi'),
                        desc="Run Rofi"))

        keys.append(
            Key([self.mod, self.control], "h", lazy.spawn(f"/usr/bin/typora /home/steve/Documents/qtilebinds.md"),
                desc="Opens this page"))

        keys.append(Key([self.mod, self.control], "l", lazy.spawn("physlock"), desc="Lock the screen"))

        return keys


class Mouse:
    def __init__(self):
        self.mod = "mod4"

    def init_mouse(self):
        mouse = [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front())
        ]
        return mouse
