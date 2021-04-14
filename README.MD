# Panoramic Image Reconstruction

[![Build Status](https://travis-ci.com/FarDust/uncropped.svg?branch=main)](https://travis-ci.com/FarDust/uncropped)

## General idea

- Use source img + depth data from Deep-AI + homography matrix
- Then stitching the image

## Traditional algorithm

As described in  \[[7](#sources)\]

- **Step 1:** Detecting keypoints (DoG, Harris, etc.) and extracting local invariant descriptors(SIFT, SURF, ORBFASTBRIEF, etc.) from multiple input images
- **Step 2:** Matching the feature descriptors between the multiple images
- **Step 3:** Estimating the homography matrixes using the set of matched features of each pair images
- **Step 4:** The warping transformation image using the homography matrix of each pair images, which are obtained from previous step

## Concepts

- Keypoints
- local invariant descriptors
- image stitching
- homography matrix
  - RANSAC algorithm
- warping transformation

## Sources

1. [image-stitching](https://www.pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python/)
2. [panoramic-reconstruction](https://medium.com/analytics-vidhya/panoramic-reconstruction-ab9fa35a38ef)
3. [image-stitching-deep-learning](https://www.kaggle.com/viswatejag/image-stiching-using-deeplearning)
4. [depth-estimation](https://paperswithcode.com/task/depth-estimation)
5. [image-stitching-datasets](https://paperswithcode.com/task/image-stitching)
6. [image-inPainting](https://github.com/1900zyh/Awesome-Image-Inpainting)
7. [deep-image-stitching](https://www.researchgate.net/publication/339671421_Deep_Feature_Extraction_for_Panoramic_Image_Stitching)
8. [keras-ResNet](https://keras.io/api/applications/resnet/)