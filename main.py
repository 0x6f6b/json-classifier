from ensurepip import version
from pathlib import Path
import json
from progress.bar import IncrementalBar

count = {
    "keys": {},
    "values": {}
}

examples = {}


def recursive_count(json_data):
    # iterate through each key and value in the json_data dictionary
    # count how many times each key and each value appears
    # if you are counting a key, add it to the count dictionary under the keys key
    # if you are counting a value, add it to the count dictionary under the values key
    # if you encounter a dictionary, call the recursive_count function on the dictionary
    for key, value in json_data.items():
        if type(value) == type(dict()):
            recursive_count(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    recursive_count(val)
        else:
            if key != "name" and key != "translation":
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
        # if the file is called "f_full_names.json" or "m_full_names.json"
        # continue to the next file in the for loop

        if path.name == "f_full_names.json" or path.name == "m_full_names.json":
            continue

        data = json.load(f)

        recursive_count(data)
    bar.next()
bar.finish()

# output the keys and values and how many times they appear in ascending order
print("Keys:")
for key, value in sorted(count["keys"].items(), key=lambda x: x[1]):
    if key != "version":
        print(key, str(value) + " | Example: " + examples[key])
    else:
        print(key, str(value))
print("Values:")
for key, value in sorted(count["values"].items(), key=lambda x: x[1]):
    if key != "1.0":
        print(key, str(value) + " | Example: " + examples[key])
    else:
        print(key, str(value))
