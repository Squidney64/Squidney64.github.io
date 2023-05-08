import json
from string import Template
from scripts.blockstate import *
from scripts.model import *
from scripts.lang import *
from scripts.loot_tables import *

# Define the number of files to create
def create_files():
    file_names = []
    with open("block_data/settings.json", "r") as f:
        settings = json.load(f)

        with open("config.json") as f:
            config = json.load(f)
        
        namespace = config["namespace"]
        folder_name = config["folder_name"]
            
        destination = get_download_path() + f"/{folder_name}/assets/{namespace}/lang/"

        filename = f"{destination}/en_us.json"

        if not os.path.exists(destination):
            os.makedirs(destination)

        # Write the contents to the file
        with open(filename, "a") as file:
            file.write('{')

        for key in settings:
            if(not key == "block_info"):
                for blockstate in settings[key]:
                    for block_name in settings[key][blockstate]:

                        is_vanilla = False
                        vanilla_var = False

                        with open("block_data/existing_blocks.json") as f:
                            vanilla_blocks = json.load(f)

                        for vb in vanilla_blocks:
                            if (settings[key][blockstate].get(block_name) == vanilla_blocks.get(vb)):
                                print("Vanilla Block Detected...")
                                is_vanilla = True
                                vanilla_var = False
                                print(f"Skipping '{settings[key][blockstate].get(block_name)}' as it is a Vanilla Block...")
                                print()
                                break
                            elif (settings[key]["block"]["block"] == vanilla_blocks.get(vb)):
                                print()
                                print("Variant of Vanilla Block Detected...")
                                is_vanilla = False
                                vanilla_var = True
                                break
                            else:
                                is_vanilla = False
                                vanilla_var = False

                        print(f"""
=================================
Creating Block: {settings[key][blockstate].get(block_name)} - {blockstate}
=================================""")

                        if (is_vanilla == False and vanilla_var == False):
                            create_blockstate_file(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), settings[key]["block"]["block"].casefold().replace(" ", "_"), blockstate, "", f"{namespace}")
                            create_model_files(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), settings[key]["block"]["block"].casefold().replace(" ", "_"), blockstate, "", f"{namespace}")
                            create_loot_tables(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), settings[key]["block"]["block"].casefold().replace(" ", "_"), blockstate, "", f"{namespace}")
                            add_to_lang(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), "", f"{namespace}")
                        elif (is_vanilla == False and vanilla_var == True):
                            create_blockstate_file(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), settings[key]["block"]["block"].casefold().replace(" ", "_"), blockstate, "", "minecraft")
                            create_model_files(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), settings[key]["block"]["block"].casefold().replace(" ", "_"), blockstate, "", "minecraft")
                            create_loot_tables(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), settings[key]["block"]["block"].casefold().replace(" ", "_"), blockstate, "", "minecraft")
                            add_to_lang(settings[key][blockstate].get(block_name).casefold().replace(" ", "_"), "", "minecraft")

        with open("config.json") as f:
            config = json.load(f)
        
        namespace = config["namespace"]
        folder_name = config["folder_name"]
            
        destination = get_download_path() + f"/{folder_name}/assets/{namespace}/lang/"

        filename = f"{destination}/en_us.json"

        if not os.path.exists(destination):
            os.makedirs(destination)

        # Write the contents to the file
        with open(filename, "a") as file:
            file.write('\n}')


# create_files()