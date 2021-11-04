from libqtile import layout

# THEME = importlib.import_module(f"themes.{current_theme}")
import themes.default as THEME


class Layouts:
    def init_layouts(self):
        """
        Returns the layouts variable
        """
        layouts = [
            layout.MonadTall(**THEME.Layout.default),
            layout.Max(**THEME.Layout.default),
            layout.floating.Floating(**THEME.Layout.default),
            # layout.TreeTab(**THEME.Layout.default),
            # layout.Stack(num_stacks=2, **THEME.Layout.default),
            # layout.Bsp(**THEME.Layout.default),
            # layout.Columns(**THEME.Layout.default),
            layout.Matrix(columns=2,**THEME.Layout.default),
            # layout.MonadWide(**THEME.Layout.default),
            # layout.RatioTile(**THEME.Layout.default),
            # layout.Tile(**THEME.Layout.default),
            # layout.VerticalTile(**THEME.Layout.default),
            # layout.Zoomy(**THEME.Layout.default),
        ]
        return layouts
