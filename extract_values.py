import os
import cv2
import pandas as pd
import numpy as np

def extract_image_properties(image):
    # Calculate the mean values of each channel (R, G, B)
    mean_rgb = image.mean(axis=(0, 1))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the contrast and brightness
    min_gray = gray.min()
    max_gray = gray.max()

    #Contrast
    hsv_image=cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
    value=hsv_image[:,:,2]
    contrast=np.std(value)


    brightness = np.mean(value)
    return mean_rgb, contrast, brightness

# Define the folder path containing the images
folder_path = 'F:\TestImages_Final-20230525T120158Z-001\TestImages_Final'

# Initialize an empty list to store the image properties
image_properties_list = []
i=0
total=len(os.listdir(folder_path))

# Iterate over the images in the folder
for file_name in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Load the image
    image = cv2.imread(file_path)

    # Extract image properties
    rgb_values, contrast, brightness = extract_image_properties(image)

    # Append the image properties to the list
    image_properties_list.append([file_name, *rgb_values, contrast, brightness])
    i+=1
    columns = ['Image', 'R', 'G', 'B', 'Contrast', 'Brightness']
    df = pd.DataFrame(image_properties_list, columns=columns)

    # Print the dataframe
    df.to_csv('test_values_x.csv')
    print(i,file_name, round((i/total*100),2),'%')

# Create a pandas dataframe from the image properties list

print(df)