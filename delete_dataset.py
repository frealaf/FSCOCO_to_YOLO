import fiftyone as fo

# Delete the existing dataset
if "fsoco-train" in fo.list_datasets():
    fo.delete_dataset("fsoco-train")
    print("Deleted existing dataset 'fsoco-train'")

# Recreate the dataset
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path="/Users/pedrotrindade/Documents/LART/fsoco/train/images",
    labels_path="/Users/pedrotrindade/Documents/LART/fsoco/train/annotations/fsoco.json",
    name="fsoco-train"
)

# Launch the FiftyOne app
fo.launch_app(dataset)