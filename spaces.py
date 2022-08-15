# recursively look through the Metadata Fixed folder

from pathlib import Path
import json
from progress.bar import IncrementalBar

# check if any double, leading or trailing spaces occur as any of the keys or values in the json file

spaces = []


def recursive_check(json_data):
    # iterate through each key and value in the json_data dictionary
    # if you encounter a dictionary, call the recursive_check function on the dictionary
    for key, value in json_data.items():
        if type(value) == type(dict()):
            recursive_check(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    recursive_check(val)
        else:
            if key in count["keys"]:
                count["keys"][key] += 1

                if "name" in json_data:
                    examples[key] = json_data["name"]
            else:
                count["keys"][key] = 1
                if "name" in json_data:
                    examples[key] = json_data["name"]

            if value in count["values"]:
                count["values"][value] += 1

                if "name" in json_data:
                    examples[value] = json_data["name"]
            else:
                count["values"][value] = 1
                if "name" in json_data:
                    examples[value] = json_data["name"]


# iterate over all files in all subdirectories and their subdirectories etc.
bar = IncrementalBar('Processing', max=len(list(Path('.').rglob('*.json'))))
for path in Path('./Metadata Fixed').rglob('*.json'):
    with open(path) as f:
        bar.next()
        # if the file is called "f_full_names.json" or "m_full_names.json"
        # continue to the next file in the for loop
        if path.name == "f_full_names.json" or path.name == "m_full_names.json":
            continue
        else:
            with open(path) as f:
                json_data = json.load(f)
                recursive_check(json_data)
bar.finish()

print("Spaces:", spaces)
