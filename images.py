import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Path to your dataset
dataset_path = 'C:/Users/Venka/OneDrive/Desktop/Image Identifier/Image-Identifer/Data'

# Function to display a few images from a folder
def display_images_from_folder(folder_name, num_images=5):
    folder_path = os.path.join(dataset_path, folder_name)
    images = os.listdir(folder_path)[:num_images]  # Limit the number of images displayed
    for img_name in images:
        img_path = os.path.join(folder_path, img_name)
        img = mpimg.imread(img_path)
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.title(img_name)
        plt.show()

# Display images from the 'cats' folder
display_images_from_folder('Dogs')
