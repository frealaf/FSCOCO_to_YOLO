## FSOCO Dataset Sanitizer and YOLOv8 Trainer
This repository is your one-stop shop for preparing the FSOCO dataset, cleaning it up, augmenting it, and training a YOLOv8 model.

Let’s get started!

## Instructions

1. Prerequisites (Before diving in, make sure you have):
	- Python 3.7 or higher
	- Virtual environment setup
	- A system that can handle YOLO training

2. Installation

	- Clone this repository
	*Tip: Make sure you’re inside the repo directory before moving on.*
  	- Set up a virtual environment
   	- Install the required libraries: should be in requirements.txt
   	  
3. Dataset Preparation

3.1 Download the FSOCO Dataset: Download the bounding boxes version from the FSOCO website.
   - Extract the dataset and ensure the directory structure matches:
     - `fsoco`
       - `train`
         - `annotations`
         - `images`

   *Organized files = Happy training!*

3.2 Convert COCO to YOLO Format: Run the `coco_to_yolov.py` script.
   *This script takes the COCO-style annotations and converts them into YOLO-style `.txt` files.*

3.3 Split into Train and Validation Sets: Run the `split_train_val.py` script to split the dataset into train and val directories.
   - `yolo_dataset`
     - `train`
       - `images`
       - `labels`
     - `val`
       - `images`
       - `labels`

**4. Data Augmentation**
The data augmentation process is currently ongoing. 

5. Visualize the Dataset
   
   	5.1 Install FiftyOne
	5.2 Run the visualization script

6. YOLOv8 Training
   
   	6.1  Create dataset.yaml
   	 - Place a dataset.yaml in the repository with the following structure:
		train: /path/to/yolo_dataset/train/images
		val: /path/to/yolo_dataset/val/images
		nc: <number_of_classes>
		names: [class1, class2, ...]
	6.2 Start Training
		- Run the YOLOv8 training command

**7. Results and Inference**
Results and inference functionalities are still pending implementation. Stay tuned for updates!






