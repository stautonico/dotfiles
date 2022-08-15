#!/usr/bin/env python3
# Ready or not mod manager

from json import loads, dumps
import os
import sys
import shutil

def create_config(config_path):
    new_config = {
        "mods": [],
        "game_dir": "",
        "standard_pak_files": ["pakchunk0-WindowsNoEditor.pak",
                               "pakchunk1-WindowsNoEditor.pak",
                               "pakchunk10-WindowsNoEditor.pak",
                               "pakchunk11-WindowsNoEditor.pak",
                               "pakchunk12-WindowsNoEditor.pak",
                               "pakchunk2-WindowsNoEditor.pak",
                               "pakchunk3-WindowsNoEditor.pak",
                               "pakchunk4-WindowsNoEditor.pak",
                               "pakchunk5-WindowsNoEditor.pak",
                               "pakchunk6-WindowsNoEditor.pak",
                               "pakchunk7-WindowsNoEditor.pak",
                               "pakchunk8-WindowsNoEditor.pak",
                               "pakchunk9-WindowsNoEditor.pak"]
        # The .pak files that are required for the base game (non-modded paks) (as of Aug 03, 2022)
    }
    save_config(new_config, config_path)

def load_config(config_path):
    try:
        with open(config_path, "r") as f:
            return loads(f.read())
    except FileNotFoundError:
        # Try to create the config and try to re-load it
        create_config(config_path)
        print(f"Created new config file at {config_path}, please set 'game_dir'")
        exit(0)

def save_config(config_obj, config_path):
    with open(config_path, "w") as f:
        f.write(dumps(config_obj))

def get_mod_name_from_pak_file(filepath, config):
    for mod in config.get("mods", []):
        if mod.get("file") == filepath:
            return mod.get("name")

    return None

def update_installed_mods(config, config_path):
    # Make sure the pak folder and the mods array are in sync
    files_in_mod_folder = [os.path.basename(x) for x in os.listdir(os.path.join(config.get("game_dir"), "ReadyOrNot", "Content", "Paks"))]

    for pak in config.get("standard_pak_files", []):
        if pak in files_in_mod_folder:
            files_in_mod_folder.remove(pak)

    for installed_mod in files_in_mod_folder:
        # Check if the installed mod exists in the config
        for mod in config.get("mods", []):
            if mod.get("file") == installed_mod:
                break
        else:
            # Its not in the config, so we have to add it
            config.get("mods").append({"file": installed_mod, "name": ""})



    # Go through all the mods in the config and remove any entries that are not installed
    for mod in config.get("mods", []):
        if mod.get("file") not in files_in_mod_folder:
            config.get("mods").remove(mod)

    save_config(config, config_path)



def list_installed_mods(config):
    files = os.listdir(os.path.join(config.get("game_dir"), "ReadyOrNot", "Content", "Paks"))
    # Remove the "standard" paks
    for pak in config.get("standard_pak_files", []):
        if pak in files:
            files.remove(pak)

    if len(files) == 0:
        print("No mods installed!")
        return

    for pak_file in files:
        mod_name = get_mod_name_from_pak_file(pak_file, config)

        if not mod_name:
            print(f"{pak_file} - Unknown mod name")
        else:
            print(f"{pak_file} - {mod_name}")

def install_mod(config, config_path):
    while True:
        file_path = input("Enter the full path to the mod (.pak) file: ")

        # Make sure the file exists
        mod_file_exists = os.path.exists(file_path)

        if not mod_file_exists:
            retry = input("Mod path does not exist, would you like to try again? [y/n]: ")
            if retry.lower() != "y":
                return
        else:
            # Check if the mod was already installed
            if (get_mod_name_from_pak_file(file_path, config)):
                print("Mod already installed!")
                return

            mod_name = input("Enter a mod name (to easily identify the mod): ")
            try:
                new_file_path = os.path.join(config.get("game_dir"), "ReadyOrNot", "Content", "Paks", os.path.basename(file_path))
                # We have to use shutil.move instead of os.rename because os.rename only works on the same fs
                # I tried to install from /tmp, and since /tmp is a tempfs, it didn't work
                shutil.move(file_path, new_file_path)
                config.get("mods").append({"file": os.path.basename(file_path), "name": mod_name})
                save_config(config, config_path)
                print(f"Successfully installed {mod_name} ({new_file_path})")
            except Exception as e:
                print(f"Failed to install mod ({e})")
            return



def uninstall_mod(config, config_path):
    if len(config.get("mods")) == 0:
        print("No mods installed!")
        return

    print("Select a mod to uninstall: ")
    for i, mod in enumerate(config.get("mods", [])):
        print(f"[{i+1}] {mod.get('name')} ({mod.get('file')})")

    to_uninstall = input(">> ")
    try:
        mod_to_uninstall = config.get("mods", [])[int(to_uninstall)-1]
        try:
            os.remove(os.path.join(config.get("game_dir"), "ReadyOrNot", "Content", "Paks", mod_to_uninstall.get("file")))
        except Exception as e:
            print(f"Failed to uninstall mod ({e})")
            return

        config.get("mods", []).remove(mod_to_uninstall)
        save_config(config, config_path)
        print(f"Successfully uninstalled mod: {mod_to_uninstall.get('name')}")
    except Exception:
        print("Invalid mod selected!")
        return



def uninstall_all_mods(config, config_path):
    for mod in config.get("mods", []):
        try:
            os.remove(os.path.join(config.get("game_dir"), "ReadyOrNot", "Content", "Paks", mod.get("file")))
        except Exception as e:
            print(f"Failed to uninstall mod ({e})")
            return

    config["mods"] = []
    save_config(config, config_path)
    print(f"Successfully uninstalled all mods!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    else:
        config_path = "./.ron_mod_man.json"
    # Load the initial config
    config = load_config(config_path)

    game_dir = config.get("game_dir")

    if not game_dir or game_dir == "":
        print("'game_dir' is invalid! Please set 'game_dir' to the location of the \"Ready or Not\" folder in your steam/steamapps/common directory.")
        exit(1)

    while True:
        print()
        print("--- Ready or Not Mod Manager ---")
        print("[1] List installed mods")
        print("[2] Install mod")
        print("[3] Uninstall mod")
        print("[4] Uninstall all mods")
        print("[5] Quit")

        user_in = input(">>? ")
        print()
        update_installed_mods(config, config_path)

        if user_in == "1":
            list_installed_mods(config)
            update_installed_mods(config, config_path)
        elif user_in == "2":
            install_mod(config, config_path)
            update_installed_mods(config, config_path)
        elif user_in == "3":
            uninstall_mod(config, config_path)
            update_installed_mods(config, config_path)
        elif user_in == "4":
            uninstall_all_mods(config, config_path)
            update_installed_mods(config, config_path)
        elif user_in in ["5", "q"]:
            print("Goodbye!")
            update_installed_mods(config, config_path)
            exit(0)
        else:
            print("Invalid input, try again!")
