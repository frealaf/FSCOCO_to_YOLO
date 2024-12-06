import os
import random
import shutil

# Paths
train_images_dir = "/Users/pedrotrindade/Documents/LART/yolo_dataset/train/images"
train_labels_dir = "/Users/pedrotrindade/Documents/LART/yolo_dataset/train/labels"
val_images_dir = "/Users/pedrotrindade/Documents/LART/yolo_dataset/val/images"
val_labels_dir = "/Users/pedrotrindade/Documents/LART/yolo_dataset/val/labels"

# Create validation directories if not exist
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Get all image files
image_files = os.listdir(train_images_dir)

# Shuffle and split
random.shuffle(image_files)
val_count = int(len(image_files) * 0.2)  # 20% for validation
val_files = image_files[:val_count]

# Move files to validation folder
for image_file in val_files:
    # Move image
    src_image = os.path.join(train_images_dir, image_file)
    dst_image = os.path.join(val_images_dir, image_file)
    shutil.move(src_image, dst_image)

    # Move corresponding label
    label_file = os.path.splitext(image_file)[0] + ".txt"
    src_label = os.path.join(train_labels_dir, label_file)
    dst_label = os.path.join(val_labels_dir, label_file)
    if os.path.exists(src_label):  # Ensure the label file exists
        shutil.move(src_label, dst_label)

print(f"Moved {val_count} images and their labels to the validation set.")