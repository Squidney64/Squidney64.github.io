import json
import os
from scripts.download import *
from recipes import *

def create_recipes(namespace, result):
    recipeType = str(input("What type of recipe is the base block? (Shapeless, shaped, smelting, smoking, blasting, campfire, stonecutting) "))

    if recipeType.casefold().strip() == "shapeless":
        Shapeless(f"{namespace}:{result}")

    elif recipeType.casefold().strip() == "shaped":
        Shaped(f"{namespace}:{result}")

    elif recipeType.casefold().strip() == "campfire":
        Smelting("campfire_cooking", f"{namespace}:{result}")
        suffix = f"_from_campfire_cooking"

    elif recipeType.casefold().strip() == "smoking":
        ingredient = Smelting("smoking", f"{namespace}:{result}")
        suffix = f"_from_smoking_{ingredient}"
    
    elif recipeType.casefold().strip() == "smelting":
        ingredient = Smelting("smelting", f"{namespace}:{result}")
        suffix = f"_from_smelting_{ingredient}"

    elif recipeType.casefold().strip() == "blasting":
        ingredient = Smelting("blasting", f"{namespace}:{result}")
        suffix = f"_from_blasting_{ingredient}"

    elif recipeType.casefold().strip() == "stonecutting":
        ingredient = Stonecutting(f"{namespace}:{result}")
        suffix = f"_from_{ingredient}_stonecutting"



    with open("config.json") as f:
        config = json.load(f)
    
    file_path = config["path"]
    namespace = config["namespace"]
    folder_name = config["folder_name"]

    if (not destination == ""):
        destination = "/" + destination
    
    destination = get_download_path() + f"/{folder_name}/assets/{namespace}/recipes{destination}"

    filename = f"{destination}/{result}{suffix}.json"

    if not os.path.exists(destination):
        os.makedirs(destination)
    