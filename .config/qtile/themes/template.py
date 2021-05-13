class Colors:
    background_one: str
    background_two: str
    background_three: str
    background_four: str
    text: str
    text_muted: str
    text_highlighted: str
    text_invert: str
    window_border: str
    widget_one: str
    widget_two: str
    widget_three: str
    widget_four: str
    widget_five: str
    widget_six: str
    widget_seven: str
    widget_eight: str
    widget_nine: str
    widget_ten: str
    border_focus: str
    border_normal: str


class Fonts:
    regular: str
    bold: str
    thin: str


class Layout:
    margin = 0
    border_width = 0
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
    fontsize = 0
    padding = 0

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
