import cv2
import os

def preprocess_images_in_folder(folder_path, output_folder, target_size=(48, 48), grayscale=True):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is an image
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Read the image
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path)
                
                # Resize the image
                image = cv2.resize(image, target_size)
                
                # Convert to grayscale if specified
                if grayscale:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                
                # Save the preprocessed image
                output_path = os.path.join(output_folder, file)
                cv2.imwrite(output_path, image)

# Example usage:
input_folder = "/Users/rakseda/Downloads/Emotion_detection_with_CNN-main/data"
output_folder = "/Users/rakseda/Downloads/Emotion_detection_with_CNN-main/data_out"
preprocess_images_in_folder(input_folder, output_folder, target_size=(48, 48), grayscale=True)


