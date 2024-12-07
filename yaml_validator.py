import yaml
import os

# Path to your dataset.yaml
yaml_path = "path/to/dataset.yaml"  # Update this to the path of your dataset.yaml file

# Validate YAML
with open(yaml_path, "r") as file:
    try:
        data = yaml.safe_load(file)
        print("YAML file is valid.")
        print(data)
    except yaml.YAMLError as e:
        print(f"Error in YAML file: {e}")

# Verify paths
for key in ["train", "val"]:
    if key in data:
        path = data[key]
        if os.path.exists(path):
            print(f"'{key}' path exists: {path}")
        else:
            print(f"'{key}' path does NOT exist: {path}")
