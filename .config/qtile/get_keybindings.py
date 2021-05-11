"""
Script that automates the process of writing a keybindings.md
By directly getting the keybindings from keybindings.py
"""

from keybindings import Keybindings, Section


def get_keybindings(generate_docs=False):
    current_keybindings = Keybindings()
    list_of_keys = list(current_keybindings.init_keys())
    if not generate_docs:
        list_of_keys = [key for key in list_of_keys if type(key) != Section]

    return list_of_keys
