import os
import json
import random
import shutil

input_json_path = r'C:\Users\Atowar\Downloads\Pedestrian_dataset_for_internship_assignment\random_sample_mavi_2_gt.json'
output_dir = r'C:\Users\Atowar\Downloads\Pedestrian_dataset_for_internship_assignment\coco_dataset'  # Base directory for COCO-style dataset
image_dir = r'C:\Users\Atowar\Downloads\Pedestrian_dataset_for_internship_assignment\Pedestrian_dataset_for_internship_assignment'

# COCO directory structure paths
train_image_dir = os.path.join(output_dir, 'train2017')
val_image_dir = os.path.join(output_dir, 'val2017')
annotation_dir = os.path.join(output_dir, 'annotations')
train_output_path = os.path.join(annotation_dir, 'instances_train2017.json')
val_output_path = os.path.join(annotation_dir, 'instances_val2017.json')

# Create the COCO directory structure
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(annotation_dir, exist_ok=True)

# Load the original JSON data
with open(input_json_path, 'r') as f:
    data = json.load(f)

# Shuffle and split images into 160 train and 40 validation
random.seed(42)
images = data["images"]
random.shuffle(images)
train_images = images[:160]
val_images = images[160:200]

# Initialize COCO format structures
train_coco_format = {
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "pedestrian"}]
}

val_coco_format = {
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "pedestrian"}]
}

annotation_id = 1

# Function to add images and annotations to COCO format
def add_images_and_annotations(image_set, coco_format, output_image_dir, annotation_check=False):
    global annotation_id
    for img in image_set:
        image_id = img["id"]
        file_name = img["file_name"]
        width = img["width"]
        height = img["height"]

        # Check if image exists in the original directory
        if os.path.exists(os.path.join(image_dir, file_name)):
            # Filter annotations for the current image
            image_annotations = [annotation for annotation in data["annotations"] if annotation["image_id"] == image_id]

            if annotation_check and len(image_annotations) == 0:
                print(f"Warning: Image {file_name} has no annotations and will be skipped.")
                continue  # Skip the image if there are no annotations

            # Copy image to the appropriate directory (train or validation)
            shutil.copy(os.path.join(image_dir, file_name), os.path.join(output_image_dir, file_name))

            # Add image information to the COCO format
            coco_format["images"].append({
                "id": image_id,
                "file_name": file_name,
                "width": width,
                "height": height
            })

            # Add annotations corresponding to this image
            for annotation in image_annotations:
                bbox = annotation["bbox"]
                coco_format["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": annotation["category_id"],
                    "bbox": bbox,
                    "area": bbox[2] * bbox[3],
                    "iscrowd": annotation.get("iscrowd", 0),
                    "segmentation": annotation.get("segmentation", []),
                    "ignore": annotation.get("ignore", 0),
                    "vis_ratio": annotation.get("vis_ratio", 1.0),
                    "height": annotation.get("height", bbox[3])
                })
                annotation_id += 1

# Add training images and annotations
add_images_and_annotations(train_images, train_coco_format, train_image_dir)

# Add validation images and annotations, ensuring that all have annotations
add_images_and_annotations(val_images, val_coco_format, val_image_dir, annotation_check=True)

# Save COCO format data (annotations JSON)
with open(train_output_path, 'w') as f:
    json.dump(train_coco_format, f, indent=4)

with open(val_output_path, 'w') as f:
    json.dump(val_coco_format, f, indent=4)

print(f"COCO train dataset saved to {train_output_path}")
print(f"COCO validation dataset saved to {val_output_path}")
