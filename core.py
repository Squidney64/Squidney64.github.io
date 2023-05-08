import json
import os
import shutil
from create import *
from scripts.recipes_core import *

def reset_settings():
    os.remove("block_data/settings.json")

    original = "block_data/settings_default.json"
    target = "block_data/settings.json"

    shutil.copyfile(original, target)

reset_settings()

def update_block_settings(dct, settings):
    """
    Recursively counts all nested dictionaries in 'dct', and creates any missing dictionaries in 'settings'.
    Then updates 'settings' to include any new keys and values from 'dct'.

    Args:
        dct (dict): Nested dictionary to be counted and merged into 'settings'.
        settings (dict): Dictionary to be updated with new keys and values from 'dct'.

    Returns:
        None
    """

    # Initialize counter for number of nested dictionaries found
    num_nested_dicts = 0

    # Iterate over all keys and values in 'dct'
    for key, value in dct.items():

        # If the value is a dictionary, recursively call the function on it
        if isinstance(value, dict):
            num_nested_dicts += 1
            update_block_settings(value, settings.setdefault(key, {}))

        # Otherwise, update 'settings' with the key and value from 'dct'
        else:
            settings[key] = value

    with open(f"block_data/settings.json", "w") as f:
        json.dump(settings, f, indent=4)

options = ""
variant = ""

# Get Block Info

with open("block_data/settings.json", "r") as f:
    settings = json.load(f)


game_version = str(input("What Minecraft version is this for? "))

print(f"""
    You Entered: {game_version}
    """)

base_block_name = str(input("What is the name of your blockset? (As seen when item is held) "))

print(f"""
    You Entered: {base_block_name}
    """)

special_block_name = str(input(f"What is the singular form of your blockset? (Leave blank to use {base_block_name}) "))

if (special_block_name == ""):
    special_block_name = base_block_name

print(f"""
    Value Set as: {special_block_name}
    """)

with open("block_data/settings.json", "w") as f:

    settings["block_info"]["version"] = game_version
    settings["block_info"]["name"] = base_block_name
    settings["block_info"]["name_singular"] = special_block_name

    json.dump(settings, f, indent=4)

# Presets

print("""
    === PRESETS ===
        Wood, Stone, Block, Colors, None
""")

selected_preset = str(input("What Preset would you like to use? "))

if("none" in selected_preset.casefold()):
    with open("block_data/settings.json", "w") as f:
        json.dump(settings, f, indent=4)

elif("block" in selected_preset.casefold()):

    block_name = base_block_name

    update_block_settings({"basic": {"block": {"block": f"{block_name}"}}}, settings)

elif("wood" in selected_preset.casefold()):

    block_name = base_block_name

    update_block_settings({"block_info":  {"do_stairs": True}}, settings)
    update_block_settings({"block_info":  {"do_slab": True}}, settings)
    update_block_settings({"block_info":  {"do_wall": True}}, settings)
    update_block_settings({"block_info":  {"do_fence": True}}, settings)
    update_block_settings({"block_info":  {"do_fence_gate": True}}, settings)
    update_block_settings({"block_info":  {"do_door": True}}, settings)
    update_block_settings({"block_info":  {"do_trapdoor": True}}, settings)
    update_block_settings({"block_info":  {"do_pressure_plate": True}}, settings)
    update_block_settings({"block_info":  {"do_button": True}}, settings)

    update_block_settings({"basic": {"block":                 {"block":           f"{block_name} Planks"}}}, settings)
    update_block_settings({"basic": {"stairs":                {"stairs":          f"{block_name} Stairs"}}}, settings)
    update_block_settings({"basic": {"slab":                  {"slab":            f"{block_name} Slab"}}}, settings)

    update_block_settings({"basic": {"fence":                 {"fence":           f"{block_name} Fence"}}}, settings)
    update_block_settings({"basic": {"fence_gate":            {"fence_gate":      f"{block_name} Fence Gate"}}}, settings)

    update_block_settings({"basic": {"door":                  {"door":            f"{block_name} Door"}}}, settings)
    update_block_settings({"basic": {"trapdoor":              {"trapdoor":        f"{block_name} Trapdoor"}}}, settings)
    update_block_settings({"basic": {"pressure_plate":        {"pressure_plate":  f"{block_name} Pressure Plate"}}}, settings)
    update_block_settings({"basic": {"button":                {"button":          f"{block_name} Button"}}}, settings)

    update_block_settings({"basic": {"block":                 {"sign":            f"{block_name} Sign"}}}, settings)
    if(game_version == "1.20"):
        update_block_settings({"basic": {"block":             {"hanging_sign":    f"{block_name} Hanging Sign"}}}, settings)

    if(str(input("Would you like to add Mosaic Wood (like bamboo)? y/n ")) == "y"):

        block_name = base_block_name + " Mosaic"
        
        update_block_settings({"mosaic": {"block":                 {"planks":          f"{block_name} Planks"}}}, settings)
        update_block_settings({"mosaic": {"stairs":                {"stairs":          f"{block_name} Stairs"}}}, settings)
        update_block_settings({"mosaic": {"slab":                  {"slab":            f"{block_name} Slab"}}}, settings)

        block_name = base_block_name

    if(str(input("Is nether-style? y/n ")) == "y"):

        update_block_settings({"basic": {"rotated_horizontal":    {"stem":            f"{block_name} Stem"}}}, settings)
        update_block_settings({"basic": {"rotated_horizontal":    {"stripped_stem":   f"Stripped {block_name} Stem"}}}, settings)
        update_block_settings({"basic": {"rotated":               {"hyphae":          f"{block_name} Hyphae"}}}, settings)
        update_block_settings({"basic": {"rotated":               {"stripped_hyphae": f"Stripped {block_name} Hyphae"}}}, settings)

        update_block_settings({"basic": {"block":                 {"fungus":          f"{block_name} Fungus"}}}, settings)
        update_block_settings({"basic": {"block":                 {"potted_fungus":   f"Potted {block_name} Fungus"}}}, settings)
        update_block_settings({"basic": {"block":                 {"wart_block":      f"{block_name} Wart Block"}}}, settings)

    else:
        
        update_block_settings({"basic": {"rotated_horizontal":    {"log":             f"{block_name} Log"}}}, settings)
        update_block_settings({"basic": {"rotated_horizontal":    {"stripped_log":    f"Stripped {block_name} Log"}}}, settings)
        update_block_settings({"basic": {"rotated":               {"wood":            f"{block_name} Wood"}}}, settings)
        update_block_settings({"basic": {"rotated":               {"stripped_wood":   f"Stripped {block_name} Wood"}}}, settings)
        
        update_block_settings({"basic": {"block":                 {"sapling":         f"{block_name} Sapling"}}}, settings)
        update_block_settings({"basic": {"block":                 {"potted_sapling":  f"Potted {block_name} Sapling"}}}, settings)
        update_block_settings({"basic": {"block":                 {"leaves":          f"{block_name} Leaves"}}}, settings)

elif("stone" in selected_preset.casefold()):

    block_name = base_block_name


    update_block_settings({"block_info":  {"do_stairs": True}}, settings)
    update_block_settings({"block_info":  {"do_slab": True}}, settings)
    update_block_settings({"block_info":  {"do_wall": True}}, settings)
    
    update_block_settings({"basic": {"block":     {"block":       f"{block_name}"}}}, settings)
    update_block_settings({"basic": {"stairs":    {"stairs":      f"{block_name} Stairs"}}}, settings)
    update_block_settings({"basic": {"slab":      {"slab":        f"{block_name} Slab"}}}, settings)
    update_block_settings({"basic": {"wall":      {"wall":        f"{block_name} Wall"}}}, settings)

    if(str(input("Add Pressure Plate and Button? y/n ")) == "y"):
            
        update_block_settings({"block_info":  {"do_pressure_plate": True}}, settings)
        update_block_settings({"block_info":  {"do_button": True}}, settings)
        update_block_settings({"basic": {"button":            {"button":          f"{block_name} Button"}}}, settings)
        update_block_settings({"basic": {"pressure_plate":    {"pressure_plate":  f"{block_name} Pressure Plate"}}}, settings)
        
    if(str(input("Add Chiseled? y/n ")) == "y"):

        update_block_settings({"block_info": {"do_chiseled": True}}, settings)
        update_block_settings({"basic": {"block": {"chiseled":    f"Chiseled {block_name}"}}}, settings)
        
    if(str(input("Add Pillar? y/n ")) == "y"):
        
        update_block_settings({"block_info": {"do_pillar": True}}, settings)
        update_block_settings({"basic": {"rotated_horizontal": {"pillar":    f"{block_name} Pillar"}}}, settings)
        
    if(str(input("Add Cracked? y/n ")) == "y"):
        
        update_block_settings({"block_info": {"do_cracked": True}}, settings)
        update_block_settings({"basic": {"block":     {"cracked":         f"Cracked {block_name}"}}}, settings)
        update_block_settings({"basic": {"stairs":    {"cracked_stairs":  f"Cracked {block_name} Stairs"}}}, settings)
        update_block_settings({"basic": {"slab":      {"cracked_slab":    f"Cracked {block_name} Slab"}}}, settings)
        update_block_settings({"basic": {"wall":      {"cracked_wall":    f"Cracked {block_name} Wall"}}}, settings)
        
    if(str(input("Add Mossy? y/n ")) == "y"):
        
        update_block_settings({"block_info": {"do_mossy": True}}, settings)
        update_block_settings({"basic": {"block":     {"mossy":           f"Mossy {block_name}"}}}, settings)
        update_block_settings({"basic": {"stairs":    {"mossy_stairs":    f"Mossy {block_name} Stairs"}}}, settings)
        update_block_settings({"basic": {"slab":      {"mossy_slab":      f"Mossy {block_name} Slab"}}}, settings)
        update_block_settings({"basic": {"wall":      {"mossy_wall":      f"Mossy {block_name} Wall"}}}, settings)
        
    if(str(input("Add Infested? y/n ")) == "y"):
        
        update_block_settings({"block_info": {"do_infested": True}}, settings)
        update_block_settings({"basic": {"block": {"infested":    f"Infested {block_name}"}}}, settings)

        if(settings["block_info"]["do_cracked"] == True):
            update_block_settings({"basic": {"block": {"infested_cracked":    f"Infested Cracked {block_name}"}}}, settings)

        if(settings["block_info"]["do_mossy"] == True):
            update_block_settings({"basic": {"block": {"infested_mossy":    f"Infested Mossy {block_name}"}}}, settings)

        if(settings["block_info"]["do_chiseled"] == True):
            update_block_settings({"basic": {"block": {"infested_chiseled":    f"Infested Chiseled {block_name}"}}}, settings)

elif("color" in selected_preset.casefold()):

    block_name = base_block_name

    update_block_settings({"block_info":  {"do_colored": True}}, settings)
    update_block_settings({"red":         {"block":   {"block":       f"Red {block_name}"}}}, settings)
    update_block_settings({"orange":      {"block":   {"block":       f"Orange {block_name}"}}}, settings)
    update_block_settings({"yellow":      {"block":   {"block":       f"Yellow {block_name}"}}}, settings)
    update_block_settings({"lime":        {"block":   {"block":       f"Lime {block_name}"}}}, settings)
    update_block_settings({"green":       {"block":   {"block":       f"Green {block_name}"}}}, settings)
    update_block_settings({"cyan":        {"block":   {"block":       f"Cyan {block_name}"}}}, settings)
    update_block_settings({"light_blue":  {"block":   {"block":       f"Light Blue {block_name}"}}}, settings)
    update_block_settings({"blue":        {"block":   {"block":       f"Blue {block_name}"}}}, settings)
    update_block_settings({"magenta":     {"block":   {"block":       f"Magenta {block_name}"}}}, settings)
    update_block_settings({"purple":      {"block":   {"block":       f"Purple {block_name}"}}}, settings)
    update_block_settings({"pink":        {"block":   {"block":       f"Pink {block_name}"}}}, settings)
    update_block_settings({"brown":       {"block":   {"block":       f"Brown {block_name}"}}}, settings)
    update_block_settings({"white":       {"block":   {"block":       f"White {block_name}"}}}, settings)
    update_block_settings({"light_gray":  {"block":   {"block":       f"Light Gray {block_name}"}}}, settings)
    update_block_settings({"gray":        {"block":   {"block":       f"Gray {block_name}"}}}, settings)
    update_block_settings({"black":       {"block":   {"block":       f"Black {block_name}"}}}, settings)

    if(str(input("Plain Inlcuded? y/n ")) == "y"):
        
        update_block_settings({"block_info":  {"do_plain": True}}, settings)
        update_block_settings({"basic":       {"block":   {"block":   f"{block_name}"}}}, settings)
       
    if(str(input("Glazed Version? y/n ")) == "y"):
        
        update_block_settings({"block_info":  {"do_glazed": True}}, settings)
        if(settings["block_info"]["do_plain"] == True):
            update_block_settings({"basic":   {"block":   {"glazed":  f"Glazed {block_name}"}}}, settings)
        update_block_settings({"red":         {"block":   {"glazed":  f"Red Glazed {block_name}"}}}, settings)
        update_block_settings({"orange":      {"block":   {"glazed":  f"Orange Glazed {block_name}"}}}, settings)
        update_block_settings({"yellow":      {"block":   {"glazed":  f"Yellow Glazed {block_name}"}}}, settings)
        update_block_settings({"lime":        {"block":   {"glazed":  f"Lime Glazed {block_name}"}}}, settings)
        update_block_settings({"green":       {"block":   {"glazed":  f"Green Glazed {block_name}"}}}, settings)
        update_block_settings({"cyan":        {"block":   {"glazed":  f"Cyan Glazed {block_name}"}}}, settings)
        update_block_settings({"light_blue":  {"block":   {"glazed":  f"Light Blue Glazed {block_name}"}}}, settings)
        update_block_settings({"blue":        {"block":   {"glazed":  f"Blue Glazed {block_name}"}}}, settings)
        update_block_settings({"magenta":     {"block":   {"glazed":  f"Magenta Glazed {block_name}"}}}, settings)
        update_block_settings({"purple":      {"block":   {"glazed":  f"Purple Glazed {block_name}"}}}, settings)
        update_block_settings({"pink":        {"block":   {"glazed":  f"Pink Glazed {block_name}"}}}, settings)
        update_block_settings({"brown":       {"block":   {"glazed":  f"Brown Glazed {block_name}"}}}, settings)
        update_block_settings({"white":       {"block":   {"glazed":  f"White Glazed {block_name}"}}}, settings)
        update_block_settings({"light_gray":  {"block":   {"glazed":  f"Light Gray Glazed {block_name}"}}}, settings)
        update_block_settings({"gray":        {"block":   {"glazed":  f"Gray Glazed {block_name}"}}}, settings)
        update_block_settings({"black":       {"block":   {"glazed":  f"Black Glazed {block_name}"}}}, settings)
        
    if(str(input("Do Stairs, Slabs, and Walls? y/n ")) == "y"):
        
        update_block_settings({"block_info":  {"do_stairs": True}}, settings)
        if(settings["block_info"]["do_plain"] == True):
            update_block_settings({"basic":   {"stairs":   {"stairs":  f"{block_name} Stairs"}}}, settings)
        update_block_settings({"red":         {"stairs":   {"stairs":  f"Red {block_name} Stairs"}}}, settings)
        update_block_settings({"orange":      {"stairs":   {"stairs":  f"Orange {block_name} Stairs"}}}, settings)
        update_block_settings({"yellow":      {"stairs":   {"stairs":  f"Yellow {block_name} Stairs"}}}, settings)
        update_block_settings({"lime":        {"stairs":   {"stairs":  f"Lime {block_name} Stairs"}}}, settings)
        update_block_settings({"green":       {"stairs":   {"stairs":  f"Green {block_name} Stairs"}}}, settings)
        update_block_settings({"cyan":        {"stairs":   {"stairs":  f"Cyan {block_name} Stairs"}}}, settings)
        update_block_settings({"light_blue":  {"stairs":   {"stairs":  f"Light Blue {block_name} Stairs"}}}, settings)
        update_block_settings({"blue":        {"stairs":   {"stairs":  f"Blue {block_name} Stairs"}}}, settings)
        update_block_settings({"magenta":     {"stairs":   {"stairs":  f"Magenta {block_name} Stairs"}}}, settings)
        update_block_settings({"purple":      {"stairs":   {"stairs":  f"Purple {block_name} Stairs"}}}, settings)
        update_block_settings({"pink":        {"stairs":   {"stairs":  f"Pink {block_name} Stairs"}}}, settings)
        update_block_settings({"brown":       {"stairs":   {"stairs":  f"Brown {block_name} Stairs"}}}, settings)
        update_block_settings({"white":       {"stairs":   {"stairs":  f"White {block_name} Stairs"}}}, settings)
        update_block_settings({"light_gray":  {"stairs":   {"stairs":  f"Light Gray {block_name} Stairs"}}}, settings)
        update_block_settings({"gray":        {"stairs":   {"stairs":  f"Gray {block_name} Stairs"}}}, settings)
        update_block_settings({"black":       {"stairs":   {"stairs":  f"Black {block_name} Stairs"}}}, settings)
        
        update_block_settings({"block_info":  {"do_slab": True}}, settings)
        if(settings["block_info"]["do_plain"] == True):
            update_block_settings({"basic":   {"slab":    {"slab":  f"{block_name} Slab"}}}, settings)
        update_block_settings({"red":         {"slab":    {"slab":  f"Red {block_name} Slab"}}}, settings)
        update_block_settings({"orange":      {"slab":    {"slab":  f"Orange {block_name} Slab"}}}, settings)
        update_block_settings({"yellow":      {"slab":    {"slab":  f"Yellow {block_name} Slab"}}}, settings)
        update_block_settings({"lime":        {"slab":    {"slab":  f"Lime {block_name} Slab"}}}, settings)
        update_block_settings({"green":       {"slab":    {"slab":  f"Green {block_name} Slab"}}}, settings)
        update_block_settings({"cyan":        {"slab":    {"slab":  f"Cyan {block_name} Slab"}}}, settings)
        update_block_settings({"light_blue":  {"slab":    {"slab":  f"Light Blue {block_name} Slab"}}}, settings)
        update_block_settings({"blue":        {"slab":    {"slab":  f"Blue {block_name} Slab"}}}, settings)
        update_block_settings({"magenta":     {"slab":    {"slab":  f"Magenta {block_name} Slab"}}}, settings)
        update_block_settings({"purple":      {"slab":    {"slab":  f"Purple {block_name} Slab"}}}, settings)
        update_block_settings({"pink":        {"slab":    {"slab":  f"Pink {block_name} Slab"}}}, settings)
        update_block_settings({"brown":       {"slab":    {"slab":  f"Brown {block_name} Slab"}}}, settings)
        update_block_settings({"white":       {"slab":    {"slab":  f"White {block_name} Slab"}}}, settings)
        update_block_settings({"light_gray":  {"slab":    {"slab":  f"Light Gray {block_name} Slab"}}}, settings)
        update_block_settings({"gray":        {"slab":    {"slab":  f"Gray {block_name} Slab"}}}, settings)
        update_block_settings({"black":       {"slab":    {"slab":  f"Black {block_name} Slab"}}}, settings)
        
        update_block_settings({"block_info":  {"do_wall": True}}, settings)
        if(settings["block_info"]["do_plain"] == True):
            update_block_settings({"basic":   {"wall":    {"wall":  f"{block_name} Wall"}}}, settings)
        update_block_settings({"red":         {"wall":    {"wall":  f"Red {block_name} Wall"}}}, settings)
        update_block_settings({"orange":      {"wall":    {"wall":  f"Orange {block_name} Wall"}}}, settings)
        update_block_settings({"yellow":      {"wall":    {"wall":  f"Yellow {block_name} Wall"}}}, settings)
        update_block_settings({"lime":        {"wall":    {"wall":  f"Lime {block_name} Wall"}}}, settings)
        update_block_settings({"green":       {"wall":    {"wall":  f"Green {block_name} Wall"}}}, settings)
        update_block_settings({"cyan":        {"wall":    {"wall":  f"Cyan {block_name} Wall"}}}, settings)
        update_block_settings({"light_blue":  {"wall":    {"wall":  f"Light Blue {block_name} Wall"}}}, settings)
        update_block_settings({"blue":        {"wall":    {"wall":  f"Blue {block_name} Wall"}}}, settings)
        update_block_settings({"magenta":     {"wall":    {"wall":  f"Magenta {block_name} Wall"}}}, settings)
        update_block_settings({"purple":      {"wall":    {"wall":  f"Purple {block_name} Wall"}}}, settings)
        update_block_settings({"pink":        {"wall":    {"wall":  f"Pink {block_name} Wall"}}}, settings)
        update_block_settings({"brown":       {"wall":    {"wall":  f"Brown {block_name} Wall"}}}, settings)
        update_block_settings({"white":       {"wall":    {"wall":  f"White {block_name} Wall"}}}, settings)
        update_block_settings({"light_gray":  {"wall":    {"wall":  f"Light Gray {block_name} Wall"}}}, settings)
        update_block_settings({"gray":        {"wall":    {"wall":  f"Gray {block_name} Wall"}}}, settings)
        update_block_settings({"black":       {"wall":    {"wall":  f"Black {block_name} Wall"}}}, settings)

variant = ""
options = ""

print("""
    === EXTRAS ===
        Stairs, Slab, Wall, Pressure Plate, Button, Chiseled, Pillar,
        Fence, Fence Gate, Door, Trapdoor, Sign, Glazed
        Cracked, Mossy, Infested, Colored

        Type "done" to continue to variants

    """)
while not "generate" in options.casefold():

    while not options.casefold() == "done":

        variant = ""
        
        if(settings["block_info"]["do_stairs"] == True):
            print(" Stairs --------- : ENABLED")
        else:
            print(" Stairs --------- : -------")
        if(settings["block_info"]["do_slab"] == True):
            print(" Slab ----------- : ENABLED")
        else:
            print(" Slab ----------- : -------")
        if(settings["block_info"]["do_wall"] == True):
            print(" Wall ----------- : ENABLED")
        else:
            print(" Wall ----------- : -------")
        if(settings["block_info"]["do_pressure_plate"] == True):
            print(" Pressure Plate - : ENABLED")
        else:
            print(" Pressure Plate - : -------")
        if(settings["block_info"]["do_button"] == True):
            print(" Button --------- : ENABLED")
        else:
            print(" Button --------- : -------")
        if(settings["block_info"]["do_chiseled"] == True):
            print(" Chiseled ------- : ENABLED")
        else:
            print(" Chiseled ------- : -------")
        if(settings["block_info"]["do_pillar"] == True):
            print(" Pillar --------- : ENABLED")
        else:
            print(" Pillar --------- : -------")
        if(settings["block_info"]["do_fence"] == True):
            print(" Fence ---------- : ENABLED")
        else:
            print(" Fence ---------- : -------")
        if(settings["block_info"]["do_fence_gate"] == True):
            print(" Fence Gate ----- : ENABLED")
        else:
            print(" Fence Gate ----- : -------")
        if(settings["block_info"]["do_door"] == True):
            print(" Door ----------- : ENABLED")
        else:
            print(" Door ----------- : -------")
        if(settings["block_info"]["do_trapdoor"] == True):
            print(" Trapdoor ------- : ENABLED")
        else:
            print(" Trapdoor ------- : -------")
        if(settings["block_info"]["do_signs"] == True):
            print(" Sign ----------- : ENABLED")
            if(settings["block_info"]["version"] == 1.20):
                print(" Hanging Signs -- : ENABLED")
        else:
            print(" Sign ----------- : -------")
            if(settings["block_info"]["version"] == 1.20):
                print(" Hanging Signs -- : -------")
        if(settings["block_info"]["do_glazed"] == True):
            print(" Glazed --------- : ENABLED")
        else:
            print(" Glazed --------- : -------")
        if(settings["block_info"]["do_cracked"] == True):
            print(" Cracked -------- : ENABLED")
        else:
            print(" Cracked -------- : -------")
        if(settings["block_info"]["do_mossy"] == True):
            print(" Mossy ---------- : ENABLED")
        else:
            print(" Mossy ---------- : -------")
        if(settings["block_info"]["do_infested"] == True):
            print(" Infested ------- : ENABLED")
        else:
            print(" Infested ------- : -------")
        if(settings["block_info"]["do_plain"] == True):
            print(" Plain Color ---- : ENABLED")
        else:
            print(" Plain Color ---- : -------")
        if(settings["block_info"]["do_colored"] == True):
            print(" Colored -------- : ENABLED")
        else:
            print(" Colored -------- : -------")

        options = str(input("""

            For Varients, what blocks should we use? (Type 'done' to continue) """))

        if("stair" in options):
            if(settings["block_info"]["do_stairs"] == True):
                update_block_settings({"block_info": {"do_stairs": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_stairs": True}}, settings)
        if("slab" in options):
            if(settings["block_info"]["do_slab"] == True):
                update_block_settings({"block_info": {"do_slab": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_slab": True}}, settings)
        if("wall" in options):
            if(settings["block_info"]["do_wall"] == True):
                update_block_settings({"block_info": {"do_wall": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_wall": True}}, settings)
        if("plate" in options):
            if(settings["block_info"]["do_pressure_plate"] == True):
                update_block_settings({"block_info": {"do_pressure_plate": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_pressure_plate": True}}, settings)
        if("button" in options):
            if(settings["block_info"]["do_button"] == True):
                update_block_settings({"block_info": {"do_button": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_button": True}}, settings)
        if("chiseled" in options):
            if(settings["block_info"]["do_chiseled"] == True):
                update_block_settings({"block_info": {"do_chiseled": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_chiseled": True}}, settings)
        if("pillar" in options):
            if(settings["block_info"]["do_pillar"] == True):
                update_block_settings({"block_info": {"do_pillar": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_pillar": True}}, settings)
                

        if("fence" in options):
            if("gate" in options):
                if(settings["block_info"]["do_fence_gate"] == True):
                    update_block_settings({"block_info": {"do_fence_gate": False}}, settings)
                else:
                    update_block_settings({"block_info": {"do_fence_gate": True}}, settings)
            else:
                if(settings["block_info"]["do_fence"] == True):
                    update_block_settings({"block_info": {"do_fence": False}}, settings)
                else:
                    update_block_settings({"block_info": {"do_fence": True}}, settings)
        if("door" in options):
            if("trapdoor" in options):
                if(settings["block_info"]["do_trapdoor"] == True):
                    update_block_settings({"block_info": {"do_trapdoor": False}}, settings)
                else:
                    update_block_settings({"block_info": {"do_trapdoor": True}}, settings)
            else:
                if(settings["block_info"]["do_door"] == True):
                    update_block_settings({"block_info": {"do_door": False}}, settings)
                else:
                    update_block_settings({"block_info": {"do_door": True}}, settings)
        if("sign" in options):
            if(settings["block_info"]["do_signs"] == True):
                update_block_settings({"block_info": {"do_signs": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_signs": True}}, settings)
        if("glaze" in options):
            if(settings["block_info"]["do_glazed"] == True):
                update_block_settings({"block_info": {"do_glazed": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_glazed": True}}, settings)
        if("cracked" in options):
            if(settings["block_info"]["do_cracked"] == True):
                update_block_settings({"block_info": {"do_cracked": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_cracked": True}}, settings)
        if("mossy" in options):
            if(settings["block_info"]["do_mossy"] == True):
                update_block_settings({"block_info": {"do_mossy": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_mossy": True}}, settings)
        if("infested" in options):
            if(settings["block_info"]["do_infested"] == True):
                update_block_settings({"block_info": {"do_infested": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_infested": True}}, settings)
        if("color" in options):
            if(settings["block_info"]["do_colored"] == True):
                update_block_settings({"block_info": {"do_colored": False}}, settings)
            else:
                update_block_settings({"block_info": {"do_colored": True}}, settings)

    while not variant.casefold() == "done":

        with open("block_data/settings.json", "w") as f:
            json.dump(settings, f, indent=4)

        print("""
            === IDEAS ===
                        (Unlisted Ideas will be act the same)
                Polished, Bricks, Polished Bricks, Tiles, Cut, Cobbled, Smooth, Dark, Etc

            === SPECIAL ===
                Block, Plant, Torch, Lantern, Campfire, Pane, Rail
                COMING SOON: Oxidized, Dead

                Type "done" to continue
                Type "options" to revisit the options
        """)

        variant = str(input("What More Variants would you like to add? "))
        print("")

        if(variant.casefold() == "done"):
            options = "generate"

        elif(variant.casefold() == "options" or variant.casefold() == "option"):
            variant = "done"
            options = ""

        elif(variant.casefold() == "block"):
            block_name = str(input("What is your block's name? "))
            print("")

            update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"block":   {"block":   f"{block_name}"}}}, settings)

        elif(variant.casefold() == "plant"):
            print("")
            plant_type = str(input("What kind of plant? (coral, flower, crop) "))
            print("")

            if(plant_type.casefold() == "flower"):

                block_name = str(input("What is your plant's name? "))
                print("")

                update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"block":   {"plant":   f"{block_name}"}}}, settings)
                
            if(plant_type.casefold() == "crop"):

                if(str(input("Is your crop 8 stages or 4? (8/4) ")) == "8"):
                    block_name = str(input("What is your plant's name? "))
                    print("")

                    update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"crop_8":   {"crop":   f"{block_name}"}}}, settings)

                else:
                    block_name = str(input("What is your plant's name? "))
                    print("")

                    update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"crop_4":   {"crop":   f"{block_name}"}}}, settings)

            if(plant_type.casefold() == "coral"):
                block_name = str(input("What is your coral's name? (Don't include Coral) "))
                print("")

                update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"block":   {"block":       f"{block_name} Coral Block"}}}, settings)
                update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"block":   {"block_dead":  f"Dead {block_name} Coral Block"}}}, settings)
                update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"block":   {"coral":       f"{block_name} Coral"}}}, settings)
                update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"block":   {"coral_dead":  f"Dead {block_name} Coral"}}}, settings)
                update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"fan":     {"fan":         f"{block_name} Coral Fan"}}}, settings)
                update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"fan":     {"fan_dead":    f"Dead {block_name} Coral Fan"}}}, settings)

        elif(variant.casefold() == "torch"):
            block_name = str(input("What is your torch's name? (Don't include torch) "))
            print("")

            update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"block":   {"torch":   f"{block_name} Torch"}}}, settings)

        elif(variant.casefold() == "lantern"):
            block_name = str(input("What is your lantern's name? (Don't include lantern) "))
            print("")

            update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"lantern":   {"lantern":   f"{block_name} Lantern"}}}, settings)

        elif(variant.casefold() == "campfire"):
            block_name = str(input("What is your campfire's name? (Don't include campfire) "))
            print("")

            update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"campfire":   {"campfire":   f"{block_name} Campfire"}}}, settings)

        elif(variant.casefold() == "Pane"):
            block_name = str(input("What is your pane's name? (Don't include pane) "))
            print("")
            special_name = str(input("What is it called? (ie. pane, bars, etc) "))
            print("")

            update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"pane":   {special_name.casefold().replace(" ", "_"):   f"{block_name} {special_name}"}}}, settings)

        elif(variant.casefold() == "rail"):
            block_name = str(input("What is your rail's name? (Don't include rail) "))
            print("")

            update_block_settings({f"{block_name.casefold().replace(' ', '_')}":  {"rail":   {"rail":   f"{block_name} Rail"}}}, settings)

        else:
            name1 = ""
            name2 = ""
            variant_detail = str(input("What detailed variant do you want (ie SMALL bricks or POLISHED bricks)? (leave blank for none) ")).casefold().title()

            print(variant)
            print(block_name)
            if(len(variant) > 1 and variant[len(variant)-1] == "s"):

                name2 = variant.casefold().title()
                name1 = block_name.casefold().title()
                name2_sing = variant[:-1].casefold().title()
            else:
                name2 = base_block_name.casefold().title()
                name1 = variant.casefold().title()
                name2_sing = special_block_name.casefold().title()

            if((name2 == "" and name2_sing == "") or name1 == ""):
                space = ""
            else:
                space = " "

            cracked = ""
            mossy = ""
            infested = ""
            color = ""

            i = 1

            if(settings["block_info"]["do_cracked"] == True):
                cracked = "Cracked "
            if(settings["block_info"]["do_mossy"] == True):
                mossy = "Mossy "
            if(settings["block_info"]["do_infested"] == True):
                infested = "Infested "
            if(settings["block_info"]["do_colored"] == True):
                red = "Red "
                orange = "Orange "
                yellow = "Yellow "
                lime = "Lime "
                green = "Green "
                cyan = "Cyan "
                light_blue = "Light Blue "
                blue = "Blue "
                magenta = "Magenta "
                purple = "Purple "
                pink = "Pink "
                brown = "Brown "
                white = "White "
                light_gray = "Light Gray "
                gray = "Gray "
                black = "Black "
                if(settings["block_info"]["do_plain"] == True):
                    i += 16
                else:
                    i += 15

            u = 0
            while u < i:
                if(not u == 100000):
                    if(u == 1):
                        color = "Red "
                    if(u == 2):
                        color = "Orange "
                    if(u == 3):
                        color = "Yellow "
                    if(u == 4):
                        color = "Lime "
                    if(u == 5):
                        color = "Green "
                    if(u == 6):
                        color = "Cyan "
                    if(u == 7):
                        color = "Light Blue "
                    if(u == 8):
                        color = "Blue "
                    if(u == 9):
                        color = "Magenta "
                    if(u == 10):
                        color = "Purple "
                    if(u == 11):
                        color = "Pink "
                    if(u == 12):
                        color = "Brown "
                    if(u == 13):
                        color = "White "
                    if(u == 14):
                        color = "Light Gray "
                    if(u == 15):
                        color = "Gray "
                    if(u == 16):
                        color = "Black "
                    if(u == 17):
                        color = ""
                
                if(settings["block_info"]["do_colored"] == True):
                    if(variant == ""):
                        if(color == ""):
                            root_dict = "basic"
                        else:
                            root_dict = f"{color[:-1].casefold().replace(' ','_')}"
                    else:
                        if(color == ""):
                            root_dict = f"{variant.casefold().replace(' ', '_')}"
                        else:
                            root_dict = f"{color.casefold().replace(' ', '_')}{variant.casefold().replace(' ', '_')}"
                elif(variant == ""):
                    root_dict = "basic"
                else:
                    root_dict = f"{color.casefold().replace(' ', '_')}{variant.casefold().replace(' ', '_')}"

                update_block_settings({root_dict:      {"block":           {"block":           f"{color}{variant_detail}{name1}{space}{name2}"}}}, settings)
                if(settings["block_info"]["do_stairs"] == True):
                    update_block_settings({root_dict:  {"stairs":          {"stairs":          f"{color}{variant_detail}{name1}{space}{name2_sing} Stairs"}}}, settings)
                if(settings["block_info"]["do_slab"] == True):
                    update_block_settings({root_dict:  {"slab":            {"slab":            f"{color}{variant_detail}{name1}{space}{name2_sing} Slab"}}}, settings)
                if(settings["block_info"]["do_wall"] == True):
                    update_block_settings({root_dict:  {"wall":            {"wall":            f"{color}{variant_detail}{name1}{space}{name2_sing} Wall"}}}, settings)
                if(settings["block_info"]["do_pressure_plate"] == True):
                    update_block_settings({root_dict:  {"pressure_plate":  {"pressure_plate":  f"{color}{variant_detail}{name1}{space}{name2_sing} Pressure Plate"}}}, settings)
                if(settings["block_info"]["do_button"] == True):
                    update_block_settings({root_dict:  {"button":          {"button":          f"{color}{variant_detail}{name1}{space}{name2_sing} Button"}}}, settings)
                if(settings["block_info"]["do_chiseled"] == True):
                    update_block_settings({root_dict:  {"block":           {"chiseled":        f"{color}{variant_detail}Chiseled {name1}{space}{name2}"}}}, settings)
                if(settings["block_info"]["do_pillar"] == True):
                    update_block_settings({root_dict:  {"rotated_horizontal":   {"pillar":     f"{color}{variant_detail}{name1}{space}{name2_sing} Pillar"}}}, settings)
                if(settings["block_info"]["do_fence"] == True):
                    update_block_settings({root_dict:  {"fence":           {"fence":           f"{color}{variant_detail}{name1}{space}{name2_sing} Fence"}}}, settings)
                if(settings["block_info"]["do_fence_gate"] == True):
                    update_block_settings({root_dict:  {"fence_gate":      {"fence_gate":      f"{color}{variant_detail}{name1}{space}{name2_sing} Pressure Plate"}}}, settings)
                if(settings["block_info"]["do_door"] == True):
                    update_block_settings({root_dict:  {"door":            {"door":            f"{color}{variant_detail}{name1}{space}{name2_sing} Door"}}}, settings)
                if(settings["block_info"]["do_trapdoor"] == True):
                    update_block_settings({root_dict:  {"trapdoor":        {"trapdoor":        f"{color}{variant_detail}{name1}{space}{name2_sing} Trapdoor"}}}, settings)
                if(settings["block_info"]["do_signs"] == True):
                    update_block_settings({root_dict:  {"sign":            {"sign":            f"{color}{variant_detail}{name1}{space}{name2_sing} Sign"}}}, settings)
                    update_block_settings({root_dict:  {"hanging_sign":    {"hanging_sign":    f"{color}{variant_detail}{name1}{space}{name2_sing} Hanging Sign"}}}, settings)
                if(settings["block_info"]["do_glazed"] == True):
                    update_block_settings({root_dict:  {"glazed":          {"glazed":          f"{color}{variant_detail}Glazed {name1}{space}{name2}"}}}, settings)

                if(settings["block_info"]["do_cracked"] == True):
                    update_block_settings({f"cracked_{root_dict}":      {"block":           {"block":           f"{cracked}{color}{variant_detail}{name1}{space}{name2}"}}}, settings)
                    if(settings["block_info"]["do_stairs"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"stairs":          {"stairs":          f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Stairs"}}}, settings)
                    if(settings["block_info"]["do_slab"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"slab":            {"slab":            f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Slab"}}}, settings)
                    if(settings["block_info"]["do_wall"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"wall":            {"wall":            f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Wall"}}}, settings)
                    if(settings["block_info"]["do_pressure_plate"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"pressure_plate":  {"pressure_plate":  f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Pressure Plate"}}}, settings)
                    if(settings["block_info"]["do_button"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"button":          {"button":          f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Button"}}}, settings)
                    if(settings["block_info"]["do_chiseled"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"block":           {"chiseled":        f"{cracked}{color}{variant_detail}Chiseled {name1}{space}{name2}"}}}, settings)
                    if(settings["block_info"]["do_pillar"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"rotated_horizontal":   {"pillar":     f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Pillar"}}}, settings)
                    if(settings["block_info"]["do_fence"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"fence":           {"fence":           f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Fence"}}}, settings)
                    if(settings["block_info"]["do_fence_gate"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"fence_gate":      {"fence_gate":      f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Pressure Plate"}}}, settings)
                    if(settings["block_info"]["do_door"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"door":            {"door":            f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Door"}}}, settings)
                    if(settings["block_info"]["do_trapdoor"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"trapdoor":        {"trapdoor":        f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Trapdoor"}}}, settings)
                    if(settings["block_info"]["do_signs"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"sign":            {"sign":            f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Sign"}}}, settings)
                        update_block_settings({f"cracked_{root_dict}":  {"hanging_sign":    {"hanging_sign":    f"{cracked}{color}{variant_detail}{name1}{space}{name2_sing} Hanging Sign"}}}, settings)
                    if(settings["block_info"]["do_glazed"] == True):
                        update_block_settings({f"cracked_{root_dict}":  {"glazed":          {"glazed":          f"{color}{variant_detail}Glazed {name1}{space}{name2}"}}}, settings)
                        
                if(settings["block_info"]["do_mossy"] == True):
                    update_block_settings({f"mossy_{root_dict}":      {"block":           {"block":           f"{mossy}{color}{variant_detail}{name1}{space}{name2}"}}}, settings)
                    if(settings["block_info"]["do_stairs"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"stairs":          {"stairs":          f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Stairs"}}}, settings)
                    if(settings["block_info"]["do_slab"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"slab":            {"slab":            f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Slab"}}}, settings)
                    if(settings["block_info"]["do_wall"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"wall":            {"wall":            f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Wall"}}}, settings)
                    if(settings["block_info"]["do_pressure_plate"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"pressure_plate":  {"pressure_plate":  f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Pressure Plate"}}}, settings)
                    if(settings["block_info"]["do_button"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"button":          {"button":          f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Button"}}}, settings)
                    if(settings["block_info"]["do_chiseled"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"block":           {"chiseled":        f"{mossy}{color}{variant_detail}Chiseled {name1}{space}{name2}"}}}, settings)
                    if(settings["block_info"]["do_pillar"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"rotated_horizontal":   {"pillar":     f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Pillar"}}}, settings)
                    if(settings["block_info"]["do_fence"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"fence":           {"fence":           f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Fence"}}}, settings)
                    if(settings["block_info"]["do_fence_gate"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"fence_gate":      {"fence_gate":      f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Pressure Plate"}}}, settings)
                    if(settings["block_info"]["do_door"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"door":            {"door":            f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Door"}}}, settings)
                    if(settings["block_info"]["do_trapdoor"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"trapdoor":        {"trapdoor":        f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Trapdoor"}}}, settings)
                    if(settings["block_info"]["do_signs"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"sign":            {"sign":            f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Sign"}}}, settings)
                        update_block_settings({f"mossy_{root_dict}":  {"hanging_sign":    {"hanging_sign":    f"{mossy}{color}{variant_detail}{name1}{space}{name2_sing} Hanging Sign"}}}, settings)
                    if(settings["block_info"]["do_glazed"] == True):
                        update_block_settings({f"mossy_{root_dict}":  {"glazed":          {"glazed":          f"{color}{variant_detail}Glazed {name1}{space}{name2}"}}}, settings)

                if(settings["block_info"]["do_infested"] == True):
                    if(settings["block_info"]["do_cracked"] == True):
                        update_block_settings({root_dict:      {"block":           {"block":           f"{infested}{cracked}{color}{variant_detail}{name1}{space}{name2}"}}}, settings)
                        if(settings["block_info"]["do_chiseled"] == True):
                            update_block_settings({root_dict:  {"block":           {"chiseled":        f"{infested}{cracked}{color}{variant_detail}Chiseled {name1}{space}{name2}"}}}, settings)

                    if(settings["block_info"]["do_mossy"] == True):
                        update_block_settings({root_dict:      {"block":           {"block":           f"{infested}{mossy}{color}{variant_detail}{name1}{space}{name2}"}}}, settings)
                        if(settings["block_info"]["do_chiseled"] == True):
                            update_block_settings({root_dict:  {"block":           {"chiseled":        f"{infested}{mossy}{color}{variant_detail}Chiseled {name1}{space}{name2}"}}}, settings)

                    update_block_settings({root_dict:      {"block":           {"infested":           f"{infested}{color}{variant_detail}{name1}{space}{name2}"}}}, settings)
                    if(settings["block_info"]["do_chiseled"] == True):
                        update_block_settings({root_dict:  {"block":           {"infested_chiseled":        f"{infested}{color}{variant_detail}Chiseled {name1}{space}{name2}"}}}, settings)
                u += 1

        with open("block_data/settings.json", "w") as f:
            json.dump(settings, f, indent=4)

        create_recipes(namespace, settings[root_dict]["block"]["block"].casefold().replace(" ", "_"))

if(options == "generate"):
    print("""
        === CREATING FILES ===
        """)

    create_files()

options = ""
variant = ""