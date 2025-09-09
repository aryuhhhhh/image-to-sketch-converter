import cv2
import os
import argparse

def image_to_sketch(input_path, output_path="output/sketch.png", intensity=256, color=False):
  
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {input_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    invert = cv2.bitwise_not(gray)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    # Invert the blurred image
    inverted_blur = cv2.bitwise_not(blur)

    # Create pencil sketch
    sketch_gray = cv2.divide(gray, inverted_blur, scale=intensity)

    if color:
        sketch_color = cv2.cvtColor(sketch_gray, cv2.COLOR_GRAY2BGR)
        sketch = cv2.multiply(sketch_color, img, scale=1/256.0)
    else:
        sketch = sketch_gray

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the sketch
    cv2.imwrite(output_path, sketch)
    print(f"✅ Sketch saved at: {output_path}")

    # Display preview
    cv2.imshow("Original Image", img)
    cv2.imshow("Sketch", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to a pencil sketch.")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("-o", "--output", default="output/sketch.png", help="Path to save sketch")
    parser.add_argument("-i", "--intensity", type=int, default=256, help="Sketch intensity (default 256)")
    parser.add_argument("-c", "--color", action="store_true", help="Enable color sketch mode")

    args = parser.parse_args()
    image_to_sketch(args.input, args.output, args.intensity, args.color)
