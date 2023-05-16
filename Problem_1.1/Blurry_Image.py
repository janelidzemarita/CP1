import cv2

def blur_image(image_path, output_path, blur_strength):
    # Load the image
    image = cv2.imread(image_path)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, blur_strength, 0)

    # Save the blurred image
    cv2.imwrite(output_path, blurred_image)

    print("Image blurred and saved successfully!")

# Example usage
input_image = "Problem_1.1/image.jpg"
output_image = "Problem_1.1/blurred_output.jpg"
blur_strength = (13, 13)  # Adjust the kernel size (odd values recommended) bigger the number, blurrier the picture
blur_image(input_image, output_image, blur_strength)
