import json
from string import Template
import os
from scripts.download import *

def create_blockstate_file(file_name, file_name_base, template, destination, vanilla_var):

    with open("config.json") as f:
        config = json.load(f)
    
    file_path = config["path"]
    namespace = config["namespace"]
    folder_name = config["folder_name"]

    if (not destination == ""):
        destination = "/" + destination
    
    print()
    destination = get_download_path() + f"/{folder_name}/assets/{namespace}/blockstates{destination}"
    print(f"Downloading At: {destination}")
    print()

    print(f" Saving File: {destination}/{file_name}.json")

    filename = f"{destination}/{file_name}.json"

    if not os.path.exists(destination):
        os.makedirs(destination)

    # Write the contents to the file
    with open(filename, "a") as file:

        d = {
            'NAMESPACE': namespace,
            'PATH': file_path,
            'BLOCK': file_name,
            'BLOCK_full': file_name_base,
        }

        with open("templates/blockstates/" + template + ".json", "r") as block:
            src = Template(block.read())
            result = src.substitute(d)
            file.write(result)
