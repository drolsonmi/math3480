<head>
<title>kMeans Algorithm</title>
<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

# The kMeans Algorithm
__Reading__
* Geron

## Clustering Algorithms

<img src="https://raw.githubusercontent.com/drolsonmi/math3480/refs/heads/main/Notes/Images/3480_ML_Landscape.png" width=550 alt="Machine Learning Landscape">

We shift gears now by looking at __unsupervised__ machine learning algorithms. These models deal with unlabelled data, meaning we don't know the outcome beforehand. With this data, we need to find patterns and groups in the data on our own.

The method of forming clusters varies from method to method
* Distances to a central point
* Distances between points
* Standard Deviations between points (KDE)
* ...

We'll look at a few of these methods. We will begin by looking at the __kMeans__ algorithm, then we will consider how to evaluate whether the model is good or not. After we look at a few methods of evaluating cluster models, we'll look at other cluster algorithms.

## kMeans
The kMeans algorithm was proposed in 1957 as a technique for pulse-code modulation (a method to digitally represent analog signals). It has become a standard in clustering models.

It is based on the idea of finding the middle of a cluster and then grouping all datapoints to the nearest cluster. Here is the basic algorithm:

1. Determine the number of centroids needed for your data
2. Randomly place the centroids throughout the data
3. Measure the distance from every point to each centroid and assign each point to the nearest centroid
4. Find the center of your clusters and move your centroids to those centers
5. Repeat steps 3-4 until points stop changing clusters

> Basic algorithm in `[19_kMeans.ipynb](./Code/19_kMeans.ipynb)`

> Using Scikit-Learn algorithm in `[19_kMeans.ipynb](./Code/19_kMeans.ipynb)`