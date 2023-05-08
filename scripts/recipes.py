import json

with open("config.json") as f:
    config = json.load(f)

namespace = config["namespace"]

def Shapeless(result):
    with open("templates/processing.json", "a") as f:
        f.write("{")
        
        f.write('''
    "type": "minecraft:crafting_shapeless",
    "group": ''')
        
        group = str(input("What block group is this recipe in? (leave blank for none) "))
        
        f.write(f'''"{group}",''')
        f.write('''\n    "ingredients": [''')

        ingCount = int(input("How many ingredients? (no more than 9) "))

        i = 1
        while not i > ingCount:

            ingName = str(input("Input your ingredient (like minecraft:stick) "))

            if ingName[0] == "#":
                ingName = ingName[1:]
                ingType = "tag"
            else:
                ingType = "item"

            f.write("\n      {")
            f.write(f'\n        "{ingType}": "{ingName}"')
            f.write("\n      }")

            if not i == ingCount:
                f.write(",")
            
            i += 1

        f.write(f'''''')

        f.write('''\n    ],''')

        f.write('\n    "result": {')
        f.write(f'\n      "item": "{result}",')
        f.write(f'\n      "count": "{int(input("How many items do you get? "))}"')
        f.write('\n    }')

        f.write("\n}")


def Shaped(result):
    with open("templates/processing.json", "a") as f:
        f.write("{")
        
        f.write('''
    "type": "minecraft:crafting_shaped",
    "group": ''')
        
        group = str(input("What block group is this recipe in? (leave blank for none) "))
        
        f.write(f'''"{group}",''')
        f.write('''\n    "pattern": [''')

        print("Remember that the patterns should have NO SPACES BETWEEN CHARACTERS. Each ingredient is represented by a unique character like #")
        row1 = str(input("Insert the pattern for the top row. "))
        row2 = str(input("Insert the pattern for the middle row. "))
        row3 = str(input("Insert the pattern for the bottom row. "))

        if not row1 == "":
            f.write(f'''\n      "{row1}"''')
            if not row2 == "" or not row3 == "":
                f.write(",")
        if not row2 == "" or (not row1 == "" and not row3 == ""):
            f.write(f'''\n      "{row2}"''')
            if not row3 == "":
                f.write(",")
        if not row3 == "":
            f.write(f'''\n      "{row3}"''')

        f.write("\n    ],")
        f.write('\n    "key": {')

        ingChars = []
        for char in row1:
            if not char in ingChars:
                ingChars += [char]
        for char in row2:
            if not char in ingChars:
                ingChars += [char]
        for char in row3:
            if not char in ingChars:
                ingChars += [char]

        for ing in ingChars:

            ingName = str(input(f"Input your ingredient for {ing} (like minecraft:stick) "))

            if ingName[0] == "#":
                ingName = ingName[1:]
                ingType = "tag"
            else:
                ingType = "item"

            f.write(f'\n      "{ing}"' + ': {')
            f.write(f'\n        "{ingType}": "{ingName}"')
            f.write("\n      }")

            if not ing == ingChars[len(ingChars) - 1]:
                f.write(",")

        f.write(f'''''')

        f.write('''\n    },''')

        f.write('\n    "result": {')
        f.write(f'\n      "item": "{result}",')
        f.write(f'\n      "count": "{int(input("How many items do you get? "))}"')
        f.write('\n    }')

        f.write("\n}")


def Smelting(variant, result):
    with open("templates/processing.json", "a") as f:
        f.write("{")
        
        f.write(f'''
    "type": "minecraft:{variant}",
    "group": ''')
        
        group = str(input("What block group is this recipe in? (leave blank for none) "))
        
        f.write(f'''"{group}",''')
        f.write('''\n    "ingredient": {''')

        ingName = str(input(f"Input your ingredient (like minecraft:stick) "))

        if ingName[0] == "#":
            ingName = ingName[1:]
            ingType = "tag"
        else:
            ingType = "item"

        f.write(f'\n      "{ingType}": "{ingName}"')

        f.write("\n    },")

        f.write('\n    "result": {')
        f.write(f'\n      "item": "{result}",')
        f.write(f'\n      "experience": "{float(input("How much xp do you get? "))}",')
        f.write(f'\n      "cookingtime": "{int(input("How much time does it take? (200 is default for smelting, 100 from blasting and smoking, 600 from campfire) "))}"')
        f.write('\n    }')

        f.write("\n}")


def Stonecutting(result):
    with open("templates/processing.json", "a") as f:
        f.write("{")
        
        f.write(f'''
    "type": "minecraft:stonecutting",
    "group": ''')
        
        group = str(input("What block group is this recipe in? (leave blank for none) "))
        
        f.write(f'''"{group}",''')
        f.write('''\n    "ingredient": {''')

        ingName = str(input(f"Input your ingredient (like minecraft:stick) "))

        if ingName[0] == "#":
            ingName = ingName[1:]
            ingType = "tag"
        else:
            ingType = "item"

        f.write(f'\n      "{ingType}": "{ingName}"')

        f.write("\n    },")

        f.write('\n    "result": {')
        f.write(f'\n      "item": "{result}",')
        f.write(f'\n      "count": "{int(input("How many items do you get? "))}",')
        f.write('\n    }')

        f.write("\n}")

        ingName = ingName.split(':', 1)[1]  # split the string at the first colon and keep everything after it

        return ingName.strip()

