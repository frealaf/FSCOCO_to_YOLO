import os
import json
import shutil

if __name__ == '__main__':

    img_count = 0 # 11572
    # 70%: 8100
    train_cap = 5000

    train_out = {"categories": list(), "images": list(), "annotations": list()}
    val_out = {"categories": list(), "images": list(), "annotations": list()}

    dataset_root_dir = "../fsoco_bounding_boxes_train"
    train_out_dir = "../fsoco/train"
    val_out_dir = "../fsoco/val"

    # open the metadata file
    f_meta = open(os.path.join(dataset_root_dir, "meta.json"))
    meta_json = f_meta.read()
    f_meta.close()
    meta_obj = json.loads(meta_json)
    valid_classes = set()
    for c in meta_obj["classes"]:
        if "seg" in c["title"]:
            continue
        train_out["categories"].append({"id": c["id"], "name": c["title"]})
        val_out["categories"].append({"id": c["id"], "name": c["title"]})
        valid_classes.add(c["id"])

    # traverse all directories and subdirectories
    for root, dirs, files in os.walk(dataset_root_dir):
        for subdir in dirs:
            # image subdirectories are called "img"
            if subdir == "img":
                full_path = os.path.join(root, subdir)
                # list images in this directory
                for img in os.listdir(full_path):

                    print("Processing image {}...".format(img))

                    # open the annotation file
                    ann_path = full_path.replace("img", "ann")
                    f = open(ann_path + "/" + img + ".json", "r")
                    ann_json = f.read()
                    f.close()
                    ann_obj = json.loads(ann_json)
                    # print(ann_obj)

                    width = ann_obj["size"]["width"]
                    height = ann_obj["size"]["height"]
                    id = ann_obj["tags"][0]["id"]

                    new_img = {"file_name": img, "width": width, "height": height, "id": id}

                    if img_count < train_cap:
                        if not os.path.exists(os.path.join(train_out_dir, "images")):
                            os.makedirs(os.path.join(train_out_dir, "images"))
                        shutil.copy(os.path.join(full_path, img), os.path.join(train_out_dir, "images", img))
                        train_out["images"].append(new_img)
                    else:
                        if not os.path.exists(os.path.join(val_out_dir, "images")):
                            os.makedirs(os.path.join(val_out_dir, "images"))
                        shutil.copy(os.path.join(full_path, img), os.path.join(val_out_dir, "images", img))
                        val_out["images"].append(new_img)

                    # iterate annotations of the current image
                    for img_ann in ann_obj["objects"]:
                        # skip segmentation classes
                        if not img_ann["classId"] in valid_classes:
                            continue

                        print("\tProcessing annotation...")
                        # compute bounding box size
                        bbox_height = img_ann["points"]["exterior"][1][1] - img_ann["points"]["exterior"][0][1]
                        bbox_width = img_ann["points"]["exterior"][1][0] - img_ann["points"]["exterior"][0][0]
                        area = bbox_width * bbox_height

                        new_ann = {"image_id": ann_obj["tags"][0]["id"], "category_id": img_ann["classId"],
                                 "bbox": [img_ann["points"]["exterior"][0][0], img_ann["points"]["exterior"][0][1],
                                          bbox_width, bbox_height], "area": area, "iscrowd": 0, "id": img_ann["id"]}

                        if img_count < train_cap:
                            train_out["annotations"].append(new_ann)
                                
                        else:
                            val_out["annotations"].append(new_ann)

                    img_count += 1

    print("Writing output annotations files...", end="")
    if not os.path.exists(os.path.join(train_out_dir, "annotations")):
        os.makedirs(os.path.join(train_out_dir, "annotations"))
    f_out = open(os.path.join(train_out_dir, "annotations/fsoco.json"), "w")
    f_out.write(json.dumps(train_out))
    f.close()

    if not os.path.exists(os.path.join(val_out_dir, "annotations")):
        os.makedirs(os.path.join(val_out_dir, "annotations"))
    f_out = open(os.path.join(val_out_dir, "annotations/fsoco.json"), "w")
    f_out.write(json.dumps(val_out))
    f.close()
    print("Done.")

    print("{} images processed.".format(img_count))
