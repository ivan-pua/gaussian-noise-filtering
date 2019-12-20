# Gaussian Blurring or Smoothing using OpenCV

Here we will discuss image noise, how to add it to an image, and how to minimize noise with Gaussian blurring using OpenCV.

An example is shown below:
### Original Image
![Original Image](https://github.com/puaqieshang/gaussian-noise-filtering/blob/master/insta.jpeg)
*Original Image - this was captured in Mount Cook, New Zealand*


### Noise Addition
![](https://github.com/puaqieshang/gaussian-noise-filtering/blob/master/withNoise.jpeg)
*Introducing noise in the image*

Image noise manifests itself as random variations in the brightness or color of pixels in an image, or speckles that are similar to film grain on analogue cameras. If image noise is significant enough, it can potentially interfere with a computer vision system’s functionality, such as the edge-detection algorithm for lane detection in a self-driving car. 

### Gaussian Blurring
![](https://github.com/puaqieshang/gaussian-noise-filtering/blob/master/blur.png)
*Gaussian Blurring smoothes out or eliminates noise, depending on kernel size*

**Kernel** - The area that is scanned around each pixel is called the kernel. A larger kernel scans a larger amount of pixels that surround the center pixel.

## Conclusion
Increasing Kernel Size and Sigma (Standard Deviation) will enhance the blurring effec; decreasing these would decrease blur
