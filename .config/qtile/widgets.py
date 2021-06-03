import os
from typing import Literal

from libqtile import bar, widget, qtile
from libqtile.config import Screen

import custom_widgets
# THEME = importlib.import_module(f"themes.{current_theme}")
import themes.default as THEME


class MyWidgets:
    def __init__(self):
        self.tilix = "/usr/bin/tilix"

    def init_widgets_list(self, monitor: Literal["left", "right"]):
        '''
        Function that returns the desired widgets in form of list
        '''

        # Common widgets shared between screens
        begin_end_separator = widget.Sep(linewidth=0, padding=7, **THEME.Widget.fgbg_default)
        after_group_separator = widget.Sep(linewidth=0, padding=15, **THEME.Widget.fgbg_default)

        current_window_name = widget.WindowName(foreground=THEME.Colors.text_highlighted,
                                                background=THEME.Colors.background_one, padding=0)
        sys_tray = widget.Systray(background=THEME.Widget.default["background"], padding=THEME.Widget.padding)
        layout_icon = widget.CurrentLayoutIcon(custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                                               **THEME.Widget.fgbg_six, padding=0,
                                               scale=0.7)
        current_layout = widget.CurrentLayout(**THEME.Widget.fgbg_six, padding=THEME.Widget.padding)

        ram_widget = widget.Memory(**THEME.Widget.fgbg_one,
                                   mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(self.tilix + ' -e htop')},
                                   padding=THEME.Widget.padding,
                                   format='RAM  | {MemUsed: .0f} MB/{MemTotal: .0f} MB ({MemPercent}%)')

        cpu_widget = widget.CPU(**THEME.Widget.fgbg_two,
                                mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(self.tilix + ' -e htop')},
                                padding=THEME.Widget.padding,
                                format='  | {load_percent}%')

        volume_widget = widget.Volume(**THEME.Widget.fgbg_default, padding=THEME.Widget.padding)

        weather_widget = widget.OpenWeather(location="New York, US", padding=THEME.Widget.padding,
                                            **THEME.Widget.fgbg_five,
                                            metric=False, update_interval=120,
                                            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                                                "/usr/bin/firefox-developer-edition https://weather.com/weather/today/l/668f899de7fd99b1a4071e9ace8335e7af628fa2314ce00462b83aad77a0d92f"),
                                                             "Button3": lambda: qtile.cmd_spawn(
                                                                 "/usr/bin/firefox-developer-edition https://openweathermap.org/city/5128581")},
                                            format="{main_temp} °{units_temperature} | {weather_details}")

        clock = widget.Clock(**THEME.Widget.fgbg_seven, format="%a, %b %-d  [ %-I:%M:%S ]")

        if monitor == "left":
            left_monitor = [
                begin_end_separator,
                widget.GroupBox(
                    font=THEME.Fonts.regular,
                    fontsize=THEME.Widget.fontsize,
                    margin_y=2,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=THEME.Colors.text_highlighted,
                    inactive=THEME.Colors.text_muted,
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    this_current_screen_border=THEME.Colors.background_two,
                    this_screen_border=THEME.Colors.background_three,
                    **THEME.Widget.fgbg_default,
                    disable_drag=True,
                    visible_groups=["L1", "L2", "L3", "Discord"]
                ),
                after_group_separator,
                current_window_name,
                sys_tray,
                begin_end_separator,
                ram_widget,
                cpu_widget,
                custom_widgets.BitcoinTicker(
                    foreground=THEME.Colors.text_invert,
                    background=THEME.Widget.fgbg_three["background"],
                    padding=THEME.Widget.padding,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                        "/usr/bin/firefox-developer-edition https://www.coindesk.com/price/bitcoin")}
                ),
                custom_widgets.EthereumTicker(
                    **THEME.Widget.fgbg_four,
                    padding=THEME.Widget.padding,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(
                        "/usr/bin/firefox-developer-edition https://www.coindesk.com/price/ethereum")}
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
                    font=THEME.Fonts.regular,
                    fontsize=THEME.Widget.fontsize,
                    margin_y=2,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=THEME.Colors.text_highlighted,
                    inactive=THEME.Colors.text_muted,
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    this_current_screen_border=THEME.Colors.background_two,
                    this_screen_border=THEME.Colors.background_three,
                    **THEME.Widget.fgbg_default,
                    disable_drag=True,
                    visible_groups=["R1", "R2", "R3", "Discord"]
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

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''

        return [Screen(top=bar.Bar(widgets=self.init_widgets_list("right"), opacity=1.00, size=20)),
                Screen(top=bar.Bar(widgets=self.init_widgets_list("left"), opacity=1.00, size=20))]
