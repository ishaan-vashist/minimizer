import os
from PIL import Image

# Define the directory path containing the images
directory = r"C:\Users\ishaa\Desktop\fist images"

# Define desired target size
desired_height = 128
desired_width = 128

# Resize images
def resize_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Add more file extensions if needed
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
            resized_image = image.resize((desired_width, desired_height))
            # Save the resized image (optional)
            resized_image.save(os.path.join(directory, f"resized_{filename}"))

# Call the function to resize images in the directory
resize_images_in_directory(directory)
