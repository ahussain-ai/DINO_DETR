import json
import os
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as patches
import random 

# Paths
test_json_path = r'C:\Users\Atowar\Downloads\Pedestrian_dataset_for_internship_assignment\coco_custom\annotations\coco_test_annotations.json'
image_dir = r'C:\Users\Atowar\Downloads\Pedestrian_dataset_for_internship_assignment\coco_custom\test_images'

# Load the COCO test annotations
with open(test_json_path, 'r') as f:
    test_data = json.load(f)

# Create a mapping from category_id to category name
category_map = {cat['id']: cat['name'] for cat in test_data['categories']}

# Function to visualize an image and its bounding boxes
def visualize_image_with_bboxes(image_id):
    # Find the image metadata using the image_id
    image_info = next(img for img in test_data['images'] if img['id'] == image_id)
    file_name = image_info['file_name']
    img_path = os.path.join(image_dir, file_name)

    # Open the image
    image = Image.open(img_path)
    fig, ax = plt.subplots(1)
    ax.imshow(image)

    # Get annotations for the image
    annotations = [ann for ann in test_data['annotations'] if ann['image_id'] == image_id]
    
    # Draw bounding boxes and class names on the image
    for ann in annotations:
        bbox = ann['bbox']  # COCO format is [x, y, width, height]
        x, y, width, height = bbox
        category_id = ann['category_id']
        category_name = category_map[category_id]

        # Create a rectangle patch for the bounding box
        rect = patches.Rectangle((x, y), width, height, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        # Annotate the bounding box with the class name
        ax.text(x, y, category_name, color='white', fontsize=12, bbox=dict(facecolor='red', alpha=0.5))

    # Display the image with bounding boxes
    plt.axis('off')  # Hide axes
    plt.show()




ids = [ image['id'] for image in random.sample(test_data['images'], k=10)]


# Test the visualization on a few images

for id in ids : 
    try :
        visualize_image_with_bboxes(id)
    except : 
        pass

