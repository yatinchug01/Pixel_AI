import cv2

def change_image_properties(image_path, contrast, brightness):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Adjust contrast and brightness
    adjusted_image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    
    # Display the original and adjusted images
    #cv2.imshow("Original Image", image)
    path = "New_"+image_path
    cv2.imwrite(path, adjusted_image)
    
   

# Example usage
change_image_properties("DSC_4999.JPG", 1.5, 0.419)
