import json
from string import Template
import os
from scripts.download import *

def create_model_files(file_name, file_name_base, template, destination, vanilla_var):

    with open("config.json") as f:
        config = json.load(f)
    
    file_path = config["path"]
    namespace = config["namespace"]
    folder_name = config["folder_name"]

    if (not destination == ""):
        destination = "/" + destination

    print()
    destination = get_download_path() + f"/{folder_name}/assets/{namespace}/models{destination}"
    print(f"Downloading At: {destination}")
    print()

    with open("templates/models/templates.json") as f:
        templates = json.load(f)

    u = 0
    for key in templates[template]:
        model_data = templates[template][u].split("/")
        u += 1

        folder = model_data[0]
        model = model_data[1]
        name_suffix = model_data[2]
        model_template = model_data[3]
        if(len(model_data) == 5):
            type = model_data[4]
        else:
            type = "texture"

        if(folder == "block"):
            filename = f"{destination}/{folder}/{file_name}{name_suffix}.json"
        else:
            filename = f"{destination}/{folder}/{file_name}.json"
        print(f" Saving File: {filename}")

        if not os.path.exists(f"{destination}/{folder}"):
            os.makedirs(f"{destination}/{folder}")

        # Write the contents to the file
        with open(filename, "a") as file:

            if(folder == "item"):
                file_name = file_name + name_suffix

            d = {
                'NAMESPACE': vanilla_var,
                'PATH': file_path,
                'BLOCK': file_name,
                'TYPE': type,
                'PARENT': model_template,
                'BLOCK_full': file_name_base,
            }

            with open("templates/models/" + folder + "/" + model + ".json", "r") as block:
                src = Template(block.read())
                result = src.substitute(d)
                file.write(result)