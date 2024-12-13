# Segmenting PASCAL VOC 2012 Dataset Variety Images Based on Contours

## I. Introduction

Image segmentation is a critical task in computer vision, enabling the identification and delineation of objects within an image. The PASCAL VOC 2012 dataset, known for its diversity and complexity, presents a challenging benchmark for segmentation tasks. Traditional segmentation methods often struggle with variations in object shapes, sizes, and lighting conditions. Contour-based segmentation, particularly with tools like OpenCV, offers a robust approach by focusing on the edges and boundaries of objects, which are key features for distinguishing different elements in an image. This project explores the application of OpenCV’s contour detection and related techniques to achieve effective segmentation of images from this dataset, addressing challenges such as noise and overlapping boundaries.


## II. Abstract

This project aims to develop a contour-based image segmentation using OpenCV to analyze and segment images from the PASCAL VOC 2012 dataset. The methodology includes preprocessing the images to enhance contours, detecting edges using techniques such as Canny Edge Detection, and leveraging OpenCV’s contour extraction functions for precise segmentation. By focusing on contours, this approach seeks to improve segmentation accuracy, especially for images with complex structures. The expected outcome is a robust segmentation framework that can be generalized to other datasets, demonstrating the potential of contour-based methods for object recognition and scene understanding.

## III. Project Methods

The proponents did the following steps:

+	Find a dataset with images
+	Learn about Segmentation and Contours
+	Learn how to implement Segmentation based on Contours
+	Search for relative methods involved
+	Make the program
+ Test the Program

## IV. Conclusion

### Findings

The proponents found the following during the project's development:

+	Contours are dependent to the edge detection
+	The more the threshold, the lesser detection
+	The blur is not adjustable based on the code due to errors

### Challenges

The proponents encountered the following challenges:

+	The proponents had a dataset but were unable to implement a form of training of data
+	The program resources were scarce due to variety of differences and uniqueness resulting in errors
+	The proponents had difficulties choosing a topic due to availability and compatibility with the topic

### Outcomes

The proponents came to the following outcomes:

+	The results of the Segmentation were satisfactory
+	The results vary per Image and adjustment
+	The desired result can be achieved with proper adjustments



## V. Additional Materials

### Code

**Figure 1.1: The code image contains two lines, which import necessary libraries for image processing and numerical operations.**

![image](https://github.com/user-attachments/assets/a05d2979-45f5-4d68-8e7f-28431de8480b)

**Figure 1.2: The code snippet loads an image and converts it to grayscale using OpenCV.**

![image](https://github.com/user-attachments/assets/687a1f03-dfd6-4235-a5d9-e0ef2bf73f06)

**Figure 1.3: The code applies a Gaussian blur to the grayscale image to reduce noise.**

![image](https://github.com/user-attachments/assets/84f39375-9f0a-46bb-af06-5f97b6105a63)

**Figure 1.4: The code detects edges in the blurred image using the Canny edge detection algorithm.**

![image](https://github.com/user-attachments/assets/41108d33-0c5e-45e0-8815-0d3a488e8455)

**Figure 1.5: The code finds contours in the edge-detected image.**

![image](https://github.com/user-attachments/assets/b239e3f5-d894-441e-9a6f-4cd301a141c0)

**Figure 1.6: The code creates a blank image and draws the found contours on it in green.**

![image](https://github.com/user-attachments/assets/9c082882-ad14-401c-9d75-986a40404c8f)

**Figure 1.7: The code displays the original image, the edge-detected image, and the image with contours drawn on it.**

![image](https://github.com/user-attachments/assets/be4f9fae-057e-445d-9d23-937cceb0ec53)

**Figure 1.8: The code waits for a key press before closing all the displayed windows.**

![image](https://github.com/user-attachments/assets/4c4e6c43-54e8-43d5-9530-af1b7171fc6d)

### Images and Results

**Figure 2.1: Test 1**

![image](https://github.com/user-attachments/assets/1ec4cee3-ae3c-4a4a-85c7-f90bda1bc64b)


**Figure 2.2: Test 2**

![image](https://github.com/user-attachments/assets/19454e34-799e-4fba-a409-fa3adb22a33a)


**Figure 2.3: Test 3**

![image](https://github.com/user-attachments/assets/b5e20595-d277-421e-a4cb-1595f59170f0)


**Figure 2.4: Test 4**

![image](https://github.com/user-attachments/assets/ecd25310-5c50-4ea1-96da-6b2fd69f067f)


**Figure 2.5: Test 5**

![image](https://github.com/user-attachments/assets/f4a140af-15fc-4b65-858e-14d1106a186b)


**Figure 2.6: Test 6**

![image](https://github.com/user-attachments/assets/ff711e33-3839-48bb-a100-19f1d7ad3f51)


**Figure 2.7: Test 7**

![image](https://github.com/user-attachments/assets/150fd3c4-b24e-4ff5-b735-24cee53961eb)


**Figure 2.8: Test 8**

![image](https://github.com/user-attachments/assets/3b6bf8d7-1932-4540-966e-bf0a755b10e8)


**Figure 2.9: Test 9**

![image](https://github.com/user-attachments/assets/2513bd6a-822f-46ef-b824-f5e8cf25d74b)


**Figure 2.10: Test 10**

![image](https://github.com/user-attachments/assets/2442b2f1-e0f4-4837-a096-08499342168a)

### Finals Video Demonstration

***Segmenting PASCAL VOC 2012 Dataset Variety Images Based on Contours | Electives 2 - Finals Demo***

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/4S6DAG0mK-Q/0.jpg)](https://www.youtube.com/watch?v=4S6DAG0mK-Q)

