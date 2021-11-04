from subprocess import call

from get_keybindings import get_keybindings
from keybindings import Section

keys = get_keybindings(generate_docs=True)

output = ""

required_spaces = 0

modifier_keys = {
    "mod4": "Super",
    "mod1": "Alt",
    "mod5": "Right Alt",
    "shift": "Shift",
    "control": "Control"
}

for key in keys:
    if type(key) == Section:
        output += f"## {key.name}\n"
        if key.description:
            output += f"#### {key.description}\n"
        output += f"---\n"
    else:
        current_line = ""
        current_line += f"* "
        for mod in key.modifiers:
            if mod in modifier_keys.keys():
                current_line += f"{modifier_keys[mod]} + "

        if current_line[-2] == "+":
            current_line = current_line[:-2]

        current_line += f"+ {key.key.title()}"

        offset = len(current_line) + 5

        if offset > required_spaces:
            required_spaces = offset

        current_line += f" <SPACES> {key.desc}\n"

        output += current_line

    split_lines = output.split("\n")

    final_output = []

    while "" in split_lines:
        split_lines.remove("")

    for line in split_lines:
        if not (line.startswith("#") or line.startswith("-")):
            spaces_to_add = required_spaces - len(line[0:line.index("<SPACES>")])
            final_output.append(line.replace('<SPACES>', ' ' * spaces_to_add))
        else:
            final_output.append(line)

    final = "\n".join(final_output)

with open("/home/steve/.config/qtile/qtilebinds.md", "w") as f:
    # noinspection PyUnboundLocalVariable
    f.write(final)

try:
    call("rmnoconfirm -rv /home/steve/.config/qtile/qtilebinds.md")
except Exception:
    pass

try:
    call("rmnoconfirm -rv /home/steve/Documents/qtilebinds.md")
except Exception:
    pass

call("ln -sf /home/steve/.config/qtile/qtilebinds.md /home/steve/Documents/qtilebinds.md".split(" "))

print(f"Finished generating docs!")
