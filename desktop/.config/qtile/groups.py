from libqtile.config import Group, Match

# These are how you refer to the groups in code
group_names = ["L1", "L2", "L3", "R1", "R2", "R3", "Discord", "Steam", "Zoom"]

# These are the labels that are visible in the bar
group_labels = ["L1", "L2", "L3", "R1", "R2", "R3", "", "", ""]


class CreateGroups:
    def init_groups(self):
        groups = []

        for x in range(len(group_names)):
            group = Group(group_names[x], layout="monadtall", label=group_labels[x])

            if group_names[x] == "Discord":
                group.matches = [Match(wm_class=["Discord", "discord", "discord", "discord-canary"])]
                group.persist = False
                group.init = False

            if group_names[x] == "Steam":
                group.matches = [Match(wm_class=["Steam", "steam"])]
                group.persist = False
                group.init = False

            if group_names[x] == "Zoom":
                group.matches = [Match("zoom", "Zoom")]
                group.persist = False
                group.init = False

            groups.append(group)

        return groups
