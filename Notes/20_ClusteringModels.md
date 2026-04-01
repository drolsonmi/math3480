<head>
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

# Clustering Models
__Reading__
* Geron, Chapter 9

__Additional Resources__
* https://www.analyticsvidhya.com/blog/2020/10/quick-guide-to-evaluation-metrics-for-supervised-and-unsupervised-machine-learning/#:~:text=The%20two%20most%20popular%20evaluation,which%20you%20will%20explore%20next.&text=The%20Silhouette%20Coefficient%20is%20defined,points%20in%20the%20same%20cluster.
* https://stats.stackexchange.com/questions/21807/evaluation-measures-of-goodness-or-validity-of-clustering-without-having-truth
* [YouTube: DataScience A-Z for Beginners and Advance: Part 41 How to Choose the Number of Clusters](https://www.youtube.com/watch?v=FqIGui0rwh4)

## Evaluation of Cluster Models
The performance of a cluster model can't be evaluated as Supervised models, which compare the model's results with pre-labeled data. However, clustering models are unsupervised, so generally have no pre-labeled to compare.

The secret will be to look at qualities of the clusters formed by the model. For example, how big are the clusters? How does the distribution of one cluster compare to other clusters? Here, we will look at external indices and internal indices.
* An __external index__ looks at the distribution and boundaries of one cluster to those of other clusters. This means we generally base the evaluation on a known cluster structure (labels).
* An __internal index__ looks at the individual cluster without any external information. This is not dependent on any pre-known structure.

A few possible evaluations:
* Within-Cluster Sum of Squares (WCSS) and the Elbow Method (See [WCSS code example](./Code/20_ClusteringModels.ipynb))
* Silhouette index
* Dunn index
* R-squared index
* Davies-Bouldin index
* Hartigan index
* Root-mean-square standard deviation (RMSSTD)

Goals:
1. Minimize distance between points in a cluster
2. Maximize distance between clusters

## WCSS and the Elbow Method
In Scikit-Learn, the KMeans algorithm uses a metric called __inertia__, which is also known as "Within-Cluster Sum of Squares" or WCSS. 
* Measure the squared distance from each point to the nearest centroid
* Take the sum of these squared distances

$$WCSS = \sum_{i=1}^k \sum_{x\in C_i} ||x-\mu_i||^2$$

The WCSS is the metric of the total squared distance from points to their centroids. We want to minimize these distances. Of course, the more centroids we have, the lower these distances will be. But that isn't always better. At some point, adding more centroids is meaningless.

This is where the __Elbow Method__ is useful.

## The Silhouette Index
Another 

$$s = \frac{b-a}{\max(a,b)}$$

where
* $a$ is the mean distance to the other instances in the same cluster (i.e., the mean intra-cluster distance)
* $b$ is the mean nearest-cluster distance (i.e., the mean distance to the instances of the next closest cluster, defined as the one that minimizes $b$, excluding the instance's own cluster)

A silhouette score will be between +1 and -1.
* $s\approx +1$ means the instance is well inside its own cluster
* $s\approx 0$ means the instance is close to the cluster boundary
* $s\approx -1$ means the instance is likely assigned to the wrong cluster

<img src="https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098125967/files/assets/mls3_0910.png" width=450 alt="Silhouette diagram example">

## Hard Clustering vs. Soft Clustering
