# FSOCO Dataset Sanitizer

This simple script reads the FSOCO dataset, which has a odd structure, and "converts it" to the same structure as the COCO dataset, to make it easier to work with the vast availability of models designed to work with this format.

## Instructions

This could me more flexible and user friendly, making that is on the to-do list, but we had the rush to have this up and running fast.

The train/validation split is hardcoded. The number of images for training is defined on the variable ```train_cap``` at the beginning of the script.

- Clone this repository.
- Place the FSOCO dataset on a directory on the same level as the repository called ```fsoco_bounding_boxes_train```. ATTENTION: You have to download the bounding boxes version, not the segmentation one.
- Create this structure of directories:
	- `fsoco`
		- `train`
			- `images`
		- `val`
- Run the script `python3 main.py`

After some time, you should have the sanitized dataset on the subdirectory `fsoco`.




