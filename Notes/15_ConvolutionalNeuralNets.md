# Convolutional Neural Networks
Reading
* Geron, Chapter 14

> Draw a picture of an image and ask students to interpret what is going on.

How do we know what is going on in the image?
* We identify pieces of the image and put the pieces in context with each other.

Can we do this with the computer?
* In our ANN we created, we built our network to recognize a boot from a 28x28 image. But can it recognize that boot from a larger image? It can if we can isolate that image from the rest of the image. This process leads us to __Convolutional Neural Networks__ (CNNs).

## Simple CNN
* Draw an image
* Draw a window
* "Summarize" the window (will explain later) and put that summary into a cell of a new matrix
* Move the window and repeat
* Continue to shift the window until the entire image is summarized

These cells summarize what is going on in each window and help us see the aspects of the image. The size of the window is determined by the user.

Is the entire image adequately described? What about the edges?
* We can add padding edges. We can add as many padding edges as we want to make the summary matrix the same size as the original image if we want.

## Filtering
What is this "Summary" we talk about? There are many ways to describe what is going on in the windows:
* Aggregate functions
* Weighted aggregate functions
* Vertical/Horizontal filters
* Corners
* ... Use your imagination ...

## Multiple Features
Most often, a single image doesn't come as a single layer. It comes in multiple "channels". The most common is *rgb* channels. In this case, the window has to pass through the same area in all channels, creating a 3D window (a hyperwindow? Yeah... a hyperwindow!!).

We can now create multiple combinations (or features) between the channels. So, just like our image started with multiple channels, our convolutional layer now has multiple feature maps (see figure 14-6 in the textbook). We can create as many feature maps as we would like.

This process can be repeated to a second convolutional layer

<img src="https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781492032632/files/assets/mls2_1406.png" width=400 alt="Figure 14-6 from textbook: Convolutional Layers with Multiple feature maps and images with three color channels">

## Pooling Layers
It is common for Convolution Layers to be accompanied with Pooling Layers. Pooling Layers function like Convolutional layers, except,
* Windows don't do filtering - only aggregating
* Goal is to create a subsample in order to reduce the computational load, memory usage, and the number of parameters

The full picture of a CNN can be seen in Figure 14-11 of the textbook.

<img src="https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781492032632/files/assets/mls2_1411.png" width=450 alt="Figure 14-11 from the textbook of the Typical CNN architecture">

[Full Visualization of CNN is process: https://www.instagram.com/reels/DK2QRXpyUUI/](https://www.instagram.com/reels/DK2QRXpyUUI/)