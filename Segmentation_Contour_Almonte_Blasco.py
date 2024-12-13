import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\Ray\Desktop\Jupyter\OPENCV\VOC2012\JPEGImages\2008_000901.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 1: Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 2: Perform Edge Detection
edges = cv2.Canny(blurred, 50, 150)  # Adjust thresholds as needed

# Step 3: Find Contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 4: Draw Contours on a blank image
contour_image = np.zeros_like(image)  # Create a blank image
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Green contours

# Display Results
cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Contours", contour_image)

# Save the output if needed
cv2.imwrite("contours_output.jpg", contour_image)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
