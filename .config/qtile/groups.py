from libqtile.config import Group
from icons import group_icons

class CreateGroups:
    def __init__(self):
        self.group_names = group_icons

    def init_groups(self):
        groups = [Group(name, layout="monadtall") for name in self.group_names]
        return groups
