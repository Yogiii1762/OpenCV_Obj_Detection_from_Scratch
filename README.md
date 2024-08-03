# Basic Object Detection and Tracking using OpenCV

This repository contains a simple implementation of object detection and tracking using YOLOv4. The project focuses on scenarios where objects do not experience occlusion, making it suitable for clear and direct tracking applications. The codebase provides a foundational approach to object detection and tracking without employing advanced algorithms like Deep SORT.

## Overview

The primary objective of this repository is to demonstrate basic object detection and tracking using the YOLOv4 model. This implementation leverages OpenCV's DNN module for detecting objects within a video stream or static images. The repository is intended for educational purposes and provides a stepping stone for further development in the field of object detection and tracking.

### Features

- **YOLOv4 Integration**: Utilizes the YOLOv4 model for efficient object detection.
- **Basic Tracking**: Implements basic object tracking for scenarios without occlusion.
- **OpenCV DNN Module**: Employs OpenCV's Deep Neural Network (DNN) module for model loading and inference.
- **Simple and Clear Codebase**: Designed for simplicity and ease of understanding.
## Configuration

You can modify the detection parameters such as confidence thresholds and non-max suppression settings in the script. Adjust the parameters to optimize performance for your specific use case.

## Code Structure

- **`code.py`**: The main script that initializes object detection and tracking.
- **`object_detection.py`**: Contains the implementation of the object detection class using YOLOv4 and OpenCV.

## Limitations

- **No Occlusion Handling**: This implementation does not handle occlusions effectively. It is designed for scenarios where objects remain visible.
- **Basic Tracking**: The tracking approach is basic and may not be suitable for complex scenarios involving fast-moving or overlapping objects.

## Future Enhancements

- **Advanced Tracking**: Consider integrating advanced tracking algorithms like Deep SORT for improved performance in complex scenarios.
- **Occlusion Handling**: Implement methods to handle occlusions and improve detection accuracy.
- **Optimization**: Optimize the code for better performance and efficiency.

