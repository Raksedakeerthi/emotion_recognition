**Emotion Detection with CNN**
This project implements a Convolutional Neural Network (CNN) to detect facial emotions using the FER2013 dataset and a custom dataset. The model is trained to classify emotions like happiness, sadness, anger, and others.

**Installation**
Ensure the required dependencies are installed:
-pip install numpy
-pip install opencv-python
-pip install keras
-pip install --upgrade tensorflow
-pip install pillow

**Dataset**
1. FER2013 Dataset
Download the FER2013 dataset from this Kaggle link.
    https://www.kaggle.com/msambare/fer2013
Place the dataset in the data folder under your project directory.
3. Custom Dataset
A custom dataset is stored in the data folder.
Preprocessing has been performed, and the processed output is stored in the data_out folder.

**Usage**
1. Train the Emotion Detector
To train the CNN model using the FER2013 dataset or the custom dataset:
   TrainEmotionDetector.py
After training, the following files will be saved in your project directory:
emotion_model.json – contains the model architecture.
emotion_model.h5 – contains the model weights.
2. Test the Emotion Detector
Run the following script to test the model on sample images or real-time webcam input:
    TestEmotionDetector.py
3. Evaluate the CNN Model
To evaluate the model's performance and generate a confusion matrix, use the evaluation script:
      EvaluateEmotionDetector.py
The script provides:
Confusion matrix
Metrics such as accuracy, precision, recall, and F1-score

**Project Structure**
Emotion_Detection_With_CNN/
│
├── TrainEmotionDetector.py       # Script to train the emotion detector
├── TestEmotionDetector.py        # Script to test the model
├── EvaluateEmotionDetector.py    # Script to evaluate the model
├── data/                         # Folder containing the original datasets
├── data_out/                     # Folder containing preprocessed datasets
├── emotion_model.json            # Saved model architecture
├── emotion_model.h5              # Saved model weights
└── README.md                     # Project documentation

**Notes**
Ensure that the datasets are properly organized in the data folder before training or testing.
GPU Support: To speed up training, ensure that TensorFlow is set up to use a GPU.
Consider applying data augmentation to improve the model's performance.
For real-time emotion detection, a webcam is required for testing with TestEmotionDetector.py.
