import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def process_image(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if the image is loaded properly
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return
    
    # Resize image if necessary
    image = cv2.resize(image, (1024, 768))
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create an empty mask
    mask = np.zeros_like(image)
    
    # Fill the mask with the detected contours
    cv2.fillPoly(mask, contours, (255, 255, 255))
    
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Save the mask
    mask_path = os.path.join(output_path, 'room_mask.png')
    cv2.imwrite(mask_path, mask)
    
    # Optionally save the image with drawn contours for visualization
    contour_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
    processed_image_path = os.path.join(output_path, 'processed_room.png')
    cv2.imwrite(processed_image_path, contour_image)
    
    return mask_path, processed_image_path

# Example usage
input_image_path = 'images/room.jpg'
output_directory = 'output'

mask_path, processed_image_path = process_image(input_image_path, output_directory)

if mask_path and processed_image_path:
    print(f'Mask saved to: {mask_path}')
    print(f'Processed image saved to: {processed_image_path}')

    # Display the results using matplotlib
    mask_image = cv2.imread(mask_path)
    processed_image = cv2.imread(processed_image_path)
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title('Mask')
    plt.imshow(cv2.cvtColor(mask_image, cv2.COLOR_BGR2RGB))
    
    plt.subplot(1, 2, 2)
    plt.title('Processed Image')
    plt.imshow(cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB))
    
    plt.show()
