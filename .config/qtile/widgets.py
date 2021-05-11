import os
from typing import Literal

from libqtile import bar, widget, qtile
from libqtile.config import Screen

import custom_widgets


# widget_defaults = dict(
#     font="Ubuntu Mono",
#     fontsize = 12,
#     padding = 2,
#     background=colors[2]
# )

# extension_defaults = widget_defaults.copy()


class MyWidgets:
    def __init__(self):
        self.colors = [["#292d3e", "#292d3e"],  # panel background
                       # background for current screen tab
                       ["#434758", "#434758"],
                       ["#ffffff", "#ffffff"],  # font color for group names
                       # border line color for current tab
                       ["#bc13fe", "#bc13fe"],  # Group down color
                       # border line color for other tab and odd widgets
                       ["#8d62a9", "#8d62a9"],
                       ["#668bd7", "#668bd7"],  # color for the even widgets
                       ["#e1acff", "#e1acff"],  # window name

                       ["#000000", "#000000"],
                       ["#AD343E", "#AD343E"],
                       ["#f76e5c", "#f76e5c"],
                       ["#F39C12", "#F39C12"],
                       ["#F7DC6F", "#F7DC6F"],
                       ["#f1ffff", "#f1ffff"],
                       ["#4c566a", "#4c566a"], ]

        self.tilix = "/usr/bin/tilix"

    def init_widgets_list(self, monitor: Literal["left", "right"]):
        '''
        Function that returns the desired widgets in form of list
        '''

        # Common widgets shared between screens
        begin_end_separator = widget.Sep(linewidth=0, padding=7, foreground=self.colors[2], background=self.colors[0])
        after_group_separator = widget.Sep(linewidth=0, padding=15, foreground=self.colors[2],
                                           background=self.colors[0])

        current_window_name = widget.WindowName(foreground=self.colors[6], background=self.colors[0], padding=0)
        sys_tray = widget.Systray(background=self.colors[0], padding=5)
        layout_icon = widget.CurrentLayoutIcon(custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                                               foreground=self.colors[0], background=self.colors[9], padding=0,
                                               scale=0.7)
        current_layout = widget.CurrentLayout(foreground=self.colors[7], background=self.colors[9], padding=5)

        ram_widget = widget.Memory(foreground=self.colors[2], background=self.colors[5],
                                   mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(self.tilix + ' -e htop')},
                                   padding=5)

        cpu_widget = widget.CPU(foreground=self.colors[2], background=self.colors[5],
                                mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(self.tilix + ' -e htop')},
                                padding=5,
                                format='CPU {load_percent}%')

        volume_widget = widget.Volume(foreground=self.colors[2], background=self.colors[5], padding=5)

        weather_widget = widget.OpenWeather(location="New York, US", padding=5, background=self.colors[8],
                                            foreground=self.colors[7], metric=False, update_interval=120,
                                            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                                                "/usr/bin/firefox-developer-edition https://weather.com/weather/today/l/668f899de7fd99b1a4071e9ace8335e7af628fa2314ce00462b83aad77a0d92f"),
                                                             "Button3": lambda: qtile.cmd_spawn(
                                                                 "/usr/bin/firefox-developer-edition https://openweathermap.org/city/5128581")},
                                            format="{main_temp} °{units_temperature} | {weather_details}")

        clock = widget.Clock(foreground=self.colors[7], background=self.colors[8], format="%a, %b %-d  [ %-I:%M:%S ]")

        if monitor == "left":
            left_monitor = [
                begin_end_separator,
                widget.GroupBox(
                    font="Noto Sans Regular",
                    fontsize=12,
                    margin_y=2,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=self.colors[-2],
                    inactive=self.colors[-1],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    this_current_screen_border=self.colors[9],
                    this_screen_border=self.colors[4],
                    other_current_screen_border=self.colors[0],
                    other_screen_border=self.colors[0],
                    foreground=self.colors[2],
                    background=self.colors[0],
                    disable_drag=True,
                    visible_groups=["L1", "L2", "L3"]
                ),
                after_group_separator,
                current_window_name,
                sys_tray,
                begin_end_separator,
                ram_widget,
                cpu_widget,
                custom_widgets.BitcoinTicker(
                    foreground=self.colors[2],
                    background=self.colors[4],
                    padding=5
                ),
                custom_widgets.EthereumTicker(
                    foreground=self.colors[2],
                    background=self.colors[4],
                    padding=5
                ),
                weather_widget,
                layout_icon,
                current_layout,
                clock,
                begin_end_separator
            ]
            return left_monitor

        elif monitor == "right":
            right_monitor = [
                begin_end_separator,
                widget.GroupBox(
                    font="Noto Sans Regular",
                    fontsize=12,
                    margin_y=2,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=self.colors[-2],
                    inactive=self.colors[-1],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    this_current_screen_border=self.colors[9],
                    this_screen_border=self.colors[4],
                    other_current_screen_border=self.colors[0],
                    other_screen_border=self.colors[0],
                    foreground=self.colors[2],
                    background=self.colors[0],
                    disable_drag=True,
                    visible_groups=["R1", "R2", "R3"]
                ),
                after_group_separator,
                current_window_name,
                ram_widget,
                cpu_widget,
                layout_icon,
                current_layout,
                clock,
                begin_end_separator
            ]
            return right_monitor

        else:
            return []

        widgets_list = [
            widget.TextBox(
                text='',
                background=self.colors[0],
                foreground=self.colors[11],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text=" 🖬",
                foreground=self.colors[7],
                background=self.colors[11],
                padding=0,
                fontsize=14
            ),
            widget.Memory(
                foreground=self.colors[7],
                background=self.colors[11],
                mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
                    self.tilix + ' -e htop')},
                padding=5
            ),
            widget.TextBox(
                text='',
                background=self.colors[11],
                foreground=self.colors[10],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text="  ",
                foreground=self.colors[7],
                background=self.colors[10],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn("pavucontrol")}
            ),
            widget.Volume(
                foreground=self.colors[7],
                background=self.colors[10],
                padding=5
            ),
            widget.TextBox(
                text='',
                background=self.colors[10],
                foreground=self.colors[9],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text='',
                foreground=self.colors[8],
                background=self.colors[9],
                padding=0,
                fontsize=37
            ),
        ]

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        return [Screen(top=bar.Bar(widgets=self.init_widgets_list("right"), opacity=1.00, size=20)),
                Screen(top=bar.Bar(widgets=self.init_widgets_list("left"), opacity=1.00, size=20))]
