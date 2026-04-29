<head>
<title>MATH 3480 Final Exam Review</title>
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

# MATH 3480 Final Review
The final exam will be on the date indicated in the [MATH 3480 Schedule](../3480_Schedule.md).

Remember that this exam also serves as the evaluation for the Data Science Certificate. The final exam in this course is an overall evaluation of how well you understand Data Science. Because of this, you will possibly see material from MATH 3080 and MATH 3280 as well as material from this semester in MATH 3480.
- [Final Exam Review for MATH 3080](https://github.com/drolsonmi/math3080/Notes/21_FinalReview.md)

## Equations to know
- MAE, SSE, MSE, RMSE, RMSLE
- Accuracy, Precision, Recall, F1-Score
- *Norms*
- WCSS (be familiar with it)
- Feature Scaling (Normalization and Standardization)

## Course Review (including MATH 3080 and MATH 3280)
Below is a summary of the topics we discussed in our class this semester. 
- Italicized items indicate topics learned in MATH 3080 and MATH 3280 that you should definitely know

### Data Science Overview
- *What is Data Science?*
- *What is a Data Scientist?*
    - *Pi-Model*
    - *Storyteller*
- Types of Machine Learning
    - Supervised and Unsupervised Models
    - Online- and Batch-Learning Models

### Machine Learning (Statistical Learning)
- The Machine Learning Process
    - *Natural Functions and Model Functions*
        - *Reducible and Irreducible Error*
        - Overfitting
    - *Data collection --> Analysis of Data (Modeling) --> Explanation (Generalization) and Evaluation*
    - *CRISP-DM*
- Data Preprocessing
    - *ETL (Extract, Transform, Load data)*
        - Load from file, webscraping, APIs
    - *Cleaning Data (Missing Data)*
        - When to drop rows/columns
        - When to fill with a value
        - When to interpolate/forward-fill/back-fill
    - Feature Engineering (Encoding)
        - Encoding (One-hot encoding, Ordinal encoding, Label encoding)
        - Creating new features/attributes/columns
- Cross Validation
- *Feature Scaling (Normalization and Standardization)*
- *EDA (Exploratory Data Analysis)*
- *Gradient Descent* :   $w' = w-\eta\nabla L$

### Regression Models
- *Purpose and Goal (When do you use Regression models?)*
- Evaluating Regression Models
    - MAE, SSE, MSE, RMSE, RMSLE, $R^2$
- *Linear Regression*
- *Multilinear Regression*
- Polynomial Regression
- Ridge and Lasso Regression

### Classification Models
- *Purpose and Goal (When do you use Classification models?)*
- Evaluating Classification Models
    - Accuracy, Precision, Recall, F1-Score
- *k-Nearest Neighbors*
    - How do you determine k?
- *Logistic Regression*
- Naive Bayes
    - Bayes' Theorem
    - What does Naive mean in this context?
- Support Vector Machines
    - Classifiers and Machines
    - Kernels
- Neural Networks
    - Activation Functions
    - Traning with Backpropagation (Gradient Descent and the Chain Rule)
    - ANNs, DNNs, and CNNs
- Decision Trees
    - Entropy and Gini Index
- Ensemble Models
    - Hard Classifications vs Soft Classifications
    - Random Forests

### Clustering Models
- *Purpose and Goal (When do you use Clustering models?)*
- Evaluating Clustering Models
    - WCSS and the Elbow Method
    - Silhouette Score
- *KMeans*
- Gaussian Mixture Models
- Hierarchical Clustering
- DBSCAN

### Natural Language Processing
- Natural Language Understanding
- Natural Language Generation
- Steps of NLP
    1. Segmentation
    2. Tokenization
	3. Stemming
	4. Lemmatization
	5. Speech tagging (Parts of sentence structures)
    6. Named Entity Tagging/Recognition (Specific items or people mentioned)
- Bag-of-words modeling
- n-grams
- Grammars

### Ethics
- *Ethical Graphing*
- Ethics in Data Science
- Responsible AI