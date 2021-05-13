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
            # layout.floating.Floating(**self.default),
            # layout.TreeTab(**self.default),
            # layout.Stack(num_stacks=2),
            # Try more layouts by unleashing below layouts.
            # layout.Bsp(),
            # layout.Columns(),
            # layout.Matrix(),
            # layout.MonadWide(**self.default),
            # layout.RatioTile(),
            # layout.Tile(),
            # layout.VerticalTile(),
            # layout.Zoomy(),
        ]
        return layouts
