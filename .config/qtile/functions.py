from libqtile.command import lazy


class Functions:
    @staticmethod
    def window_to_previous_screen():
        @lazy.function
        def __inner(qtile):
            i = qtile.screens.index(qtile.current_screen)
            if i != 0:
                group = qtile.screens[i - 1].group.name
                qtile.current_window.togroup(group)

        return __inner

    @staticmethod
    def window_to_next_screen():
        @lazy.function
        def __inner(qtile):
            i = qtile.screens.index(qtile.current_screen)
            if i + 1 != len(qtile.screens):
                group = qtile.screens[i + 1].group.name
                qtile.current_window.togroup(group)

        return __inner

    @staticmethod
    def go_to_group(group):
        def __inner(qtile):
            from libqtile.log_utils import logger
            logger.warning(f"Our current group is {group}")
            # Left monitor is monitor 1
            # Right monitor is monitor 0
            if group in ["L1", "L2", "L3"]:
                qtile.cmd_to_screen(1)
                # qtile.switch_to_group(group)
                qtile.groups_map[group].cmd_toscreen()
            elif group in ["R1", "R2", "R3"]:
                qtile.cmd_to_screen(0)
                # qtile.switch_to_group(group)
                qtile.groups_map[group].cmd_toscreen()

        return __inner
