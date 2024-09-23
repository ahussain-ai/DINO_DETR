# DINO-DETR Object Detection

## Overview

This repository contains code and resources for training and evaluating the DINO-DETR model for object detection tasks. The model uses MultiScaleDeformableAttention and is designed to detect objects of various sizes effectively.

## Execution Steps

To execute the code, follow these steps:

1. **Clone the DINO-DETR repository** from the link provided.
   
2. **Set up the environment**:
   - Follow the instructions in the repository to install dependencies and execute the script for MultiScaleDeformableAttention.

3. **Download the dataset** from the following link:
   [Dataset Download](https://drive.google.com/drive/folders/1FhQ6tug9ti7OHXbt6-4BbmjFaMjyBYNN?usp=drive_link)

4. **Download the R50 – scale 4 model** from here:
   [R50 Scale 4 Model](https://drive.google.com/file/d/1AwUn5EebmmLBo7njjW_Ng1q9zDrqkNbB/view?usp=drive_link)

5. **Run the code**:
   - Execute each cell one by one in your preferred environment to receive the results.

## Validation Data Analysis

### Average Precision (AP) Metrics

- **AP is the primary metric for object detection**, calculating precision at various recall thresholds, averaged across Intersection over Union (IoU) thresholds between 0.50 and 0.95 (in 0.05 increments).

#### Initial Validation Results

- **AP@[IoU=0.50:0.95] for all areas**: 0.502  
  This indicates the model's overall accuracy in detecting objects across varying IoU thresholds.
  
- **AP@[IoU=0.50] for all areas**: 0.833  
  Suggests that the model can accurately detect objects with some localization tolerance.
  
- **AP@[IoU=0.75] for all areas**: 0.548  
  Indicates moderate accuracy in tightly localizing objects.
  
- **AP@[IoU=0.50:0.95] for object sizes**:
  - Small objects: **0.402**
  - Medium objects: **0.637**
  - Large objects: **0.849**

**Conclusion**: The precision for larger objects is significantly higher (84.9%) than for smaller ones (40.2%).

### Validation Results After Fine-Tuning (5 Epochs)

- **Average Precision (AP)**:
  - **AP@[IoU=0.50:0.95] for all areas**: 0.559  
    Indicates an overall improvement in the model's ability to detect objects compared to the previous score of 0.502.
  
  - **AP@[IoU=0.50] for all areas**: 0.890  
    A significant increase from 0.833, showing high effectiveness in detecting objects with some localization tolerance.
  
  - **AP@[IoU=0.75] for all areas**: 0.637  
    Improved from 0.548, indicating better performance in accurately localizing objects.

- **AP for different object sizes**:
  - Small: **0.466** (improvement from 0.402)
  - Medium: **0.688** (improvement from 0.637)
  - Large: **0.874** (up from 0.849)

**Conclusion**: The model's performance after fine-tuning shows a slight improvement in accuracy, especially for small objects in our dataset.



## Acknowledgments

We thank the contributors of the DINO-DETR repository and the developers of the MultiScaleDeformableAttention framework for their invaluable work.
