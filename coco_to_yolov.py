import os
import json
from shutil import copyfile

# Paths
coco_annotations = "path/to/annotations/fsoco.json"  # Update this to the COCO annotations file path
images_dir = "path/to/annotations/fsoco.json"  # Update this to the COCO annotations file path
output_dir = "path/to/output/yolo_dataset"  # Update this to your desired output directory

# Create YOLO directory structure
os.makedirs(os.path.join(output_dir, "train", "images"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "train", "labels"), exist_ok=True)

# Load COCO annotations
with open(coco_annotations, "r") as f:
    coco_data = json.load(f)

# Map category IDs to YOLO class indices
categories = {cat["id"]: idx for idx, cat in enumerate(coco_data["categories"])}

# Convert annotations
for image in coco_data["images"]:
    image_name = image["file_name"]
    image_id = image["id"]
    label_file = os.path.splitext(image_name)[0] + ".txt"

    # Copy the image to YOLO structure
    src_image_path = os.path.join(images_dir, image_name)
    dst_image_path = os.path.join(output_dir, "train", "images", image_name)
    copyfile(src_image_path, dst_image_path)

    # Create a label file
    with open(os.path.join(output_dir, "train", "labels", label_file), "w") as label_file:
        for ann in coco_data["annotations"]:
            if ann["image_id"] == image_id:
                category_id = categories[ann["category_id"]]
                bbox = ann["bbox"]
                x_center = (bbox[0] + bbox[2] / 2) / image["width"]
                y_center = (bbox[1] + bbox[3] / 2) / image["height"]
                width = bbox[2] / image["width"]
                height = bbox[3] / image["height"]

                # Write YOLO format: class x_center y_center width height
                label_file.write(f"{category_id} {x_center} {y_center} {width} {height}\n")

print(f"YOLO dataset created at {output_dir}")
