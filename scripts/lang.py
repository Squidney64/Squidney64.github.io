import json
from string import Template
import os
from scripts.download import *

def add_to_lang(file_name, destination, vanilla_var):

    with open("config.json") as f:
        config = json.load(f)
    
    namespace = config["namespace"]
    folder_name = config["folder_name"]


    if (not destination == ""):
        destination = "/" + destination
        
    destination = get_download_path() + f"/{folder_name}/assets/{namespace}/lang/{destination}"

    filename = f"{destination}/en_us.json"

    if not os.path.exists(destination):
        os.makedirs(destination)

    with open(filename, "r") as f:
        if(f.read() == "{"):
            beginning = True
        else:
            beginning = False

    # Write the contents to the file
    with open(filename, "a") as file:
        file_name_readable = file_name.replace("_"," ").title()
        if(beginning == False):
            file.write(",")
        file.write("\n")
        file.write(f'   "block.{namespace}.{file_name}": "{file_name_readable}"')
