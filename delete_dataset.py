import fiftyone as fo

# Delete the existing dataset
if "fsoco-train" in fo.list_datasets():
    fo.delete_dataset("fsoco-train")
    print("Deleted existing dataset 'fsoco-train'")

# Recreate the dataset
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path="path/to/train/images",  # Update this to the path of your training images
    labels_path="path/to/train/annotations/fsoco.json",  # Update this to the path of your annotations file
    name="fsoco-train"
)

# Launch the FiftyOne app
fo.launch_app(dataset)
