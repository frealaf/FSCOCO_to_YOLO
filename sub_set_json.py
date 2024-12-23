import json
import os

# Paths to your dataset
original_annotations_path = "path/to/train/annotations/fsoco.json"  # Update this to the path of your original COCO annotations file
subset_images_dir = "path/to/test_subset/images"  # Update this to the directory containing the subset images
output_annotations_path = "path/to/test_subset/annotations/fsoco.json"  # Update this to the output path for the smaller annotations file

# Get the filenames of the subset images
subset_filenames = set(os.listdir(subset_images_dir))

# Load the original COCO annotations
with open(original_annotations_path, "r") as f:
    coco_data = json.load(f)

# Filter images
filtered_images = [
    img for img in coco_data["images"] if img["file_name"] in subset_filenames
]
filtered_image_ids = {img["id"] for img in filtered_images}

# Filter annotations
filtered_annotations = [
    ann for ann in coco_data["annotations"] if ann["image_id"] in filtered_image_ids
]

# Keep categories unchanged
filtered_categories = coco_data["categories"]

# Create the new COCO JSON
filtered_coco_data = {
    "images": filtered_images,
    "annotations": filtered_annotations,
    "categories": filtered_categories,
}

# Save the smaller annotations file
with open(output_annotations_path, "w") as f:
    json.dump(filtered_coco_data, f, indent=4)

print(f"Smaller dataset created at {output_annotations_path}")
