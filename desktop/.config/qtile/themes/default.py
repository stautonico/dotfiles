class Colors:
    background_one: str = "#25252d"
    background_two: str = "#3b3b47"
    background_three: str = "#050505"
    background_four: str = "#3b3b47"
    text: str = "#FFFFFF"
    text_muted: str = "#757575"
    text_highlighted: str = "#5d5dfb"
    text_invert: str = "#000000"
    window_border: str = "#bf0000"
    widget_one: str = "#bf0000"
    widget_two: str = "#bf5f00"
    widget_three: str = "#bfbf00"
    widget_four: str = "#00bf00"
    widget_five: str = "#0000bf"
    widget_six: str = "#380061"
    widget_seven: str = "#6e009e"
    widget_eight: str = "#FFFFFF"
    widget_nine: str = "#FFFFFF"
    widget_ten: str = "#FFFFFF"
    border_focus: str = "#E00000"
    border_normal: str = "#25252d"


class Fonts:
    regular: str = "Noto Sans Regular"
    bold: str = "Noto Sans Bold"
    thin: str = "Noto Sans Thin"


class Layout:
    margin = 8
    border_width = 2
    border_focus = Colors.border_focus
    border_normal = Colors.border_normal

    default = {
        "margin": margin,
        "border_width": border_width,
        "border_focus": border_focus,
        "border_normal": border_normal
    }


class Widget:
    foreground = Colors.text
    background = Colors.background_one
    font = Fonts.regular
    fontsize = 12
    padding = 5

    fgbg_default = {"foreground": foreground, "background": background}
    fgbg_one = {"foreground": foreground, "background": Colors.widget_one}
    fgbg_two = {"foreground": foreground, "background": Colors.widget_two}
    fgbg_three = {"foreground": foreground, "background": Colors.widget_three}
    fgbg_four = {"foreground": foreground, "background": Colors.widget_four}
    fgbg_five = {"foreground": foreground, "background": Colors.widget_five}
    fgbg_six = {"foreground": foreground, "background": Colors.widget_six}
    fgbg_seven = {"foreground": foreground, "background": Colors.widget_seven}
    fgbg_eight = {"foreground": foreground, "background": Colors.widget_eight}
    fgbg_nine = {"foreground": foreground, "background": Colors.widget_nine}
    fgbg_ten = {"foreground": foreground, "background": Colors.widget_ten}

    default = {
        "foreground": Colors.text,
        "background": Colors.background_one,
        "font": Fonts.regular,
        "fontsize": fontsize,
        "padding": padding
    }
