import json

# Path to the COCO annotations file
coco_annotations = "path/to/train/annotations/fsoco.json"  # Update this to the path of your COCO annotations file

# Load the annotations
with open(coco_annotations, "r") as f:
    coco_data = json.load(f)

# Extract categories
categories = coco_data["categories"]
class_names = [category["name"] for category in categories]

# Print the results
print(f"Number of classes: {len(categories)}")
print(f"Class names: {class_names}")
