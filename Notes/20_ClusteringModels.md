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
* Geron

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


## The Silhouette Index

## Hard Clustering vs. Soft Clustering
