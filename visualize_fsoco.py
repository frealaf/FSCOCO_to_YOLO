import fiftyone as fo

# Enable debug mode
fo.config.show_progress_bars = True
fo.config.debug = True

# Paths to the dataset
train_images_dir = "/Users/pedrotrindade/Documents/LART/fsoco/train/images"
train_annotations_path = "/Users/pedrotrindade/Documents/LART/fsoco/train/annotations/fsoco.json"

# Load the dataset into FiftyOne
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=train_images_dir,
    labels_path=train_annotations_path,
    name="fsoco-train_2",
    overwrite=True  # Ensures any previous dataset with the same name is replaced
)

# Launch the FiftyOne app
session = fo.launch_app(dataset)

print(dataset)