# Minimizer: Hand Gesture Recognition

## Overview
Minimizer is a hand gesture recognition system focused on detecting fist gestures. This project provides tools for training, testing, and deploying a gesture detection model, along with utilities for image preprocessing and resizing.

## Features
- **Fist Detection**: Implements a model to detect fist gestures in images.
- **Gesture Recognition Model**: Scripts to train and evaluate a hand gesture recognition model.
- **Image Preprocessing**: Tools for resizing images to prepare datasets.

## Directory Structure
```
minimizer-main/
├── fist_detect.py           # Script for fist detection
├── hand_gesture_model.py    # Model management for hand gestures
├── resizer.py               # Image resizing utility
├── test.py                  # Script for testing the model
├── train_gesture_model.py   # Script for training the model
├── fist detector/           # Contains main application scripts
│   └── minimizer.py         # Main fist detection application
├── fist images/             # Dataset for training and testing
│   ├── fist/                # Images of fists
│   └── no_fist/             # Images without fists
├── gestrure/                # Additional gesture-related images
└── ...
```

## Prerequisites
- Python 3.8+
- Required Python Libraries:
  - OpenCV
  - TensorFlow/Keras
  - NumPy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/minimizer.git
   cd minimizer-main
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Training the Model
Train the gesture recognition model using the training script:
```bash
python train_gesture_model.py
```

### 2. Testing the Model
Run tests to evaluate model performance:
```bash
python test.py
```

### 3. Running the Application
Start the fist detection application:
```bash
python fist_detect.py
```

### 4. Resizing Images
Resize images for dataset preparation:
```bash
python resizer.py
```

## Dataset
The dataset is organized into `fist` and `no_fist` categories in the `fist images/` directory. Ensure the dataset is adequately labeled before training.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact [ishaanvashista@gmail.com].

