import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris



# Initialize parameters for the decision boundary
# Starting with a vertical line around petal_length = 3
# Decision boundary: w1*x1 + w2*x2 + b = 0
# We'll start with a vertical line, then optimize

def compute_margin(w, b, X, y):
    """Compute the margin and check if all points are correctly classified"""
    distances = y * (X @ w + b)
    min_distance = np.min(distances)
    
    # Check if all points are on the correct side
    if min_distance <= 0:
        return -1, False  # Invalid separator
    
    margin = min_distance / np.linalg.norm(w)
    return margin, True

def plot_decision_boundary(w, b, margin_width, title, X, y_binary):
    """Plot the decision boundary and margins"""
    plt.figure(figsize=(10, 6))
    
    # Plot points
    setosa_mask = y_binary == -1
    other_mask = y_binary == 1
    
    plt.scatter(X[setosa_mask, 0], X[setosa_mask, 1], 
                c='blue', marker='o', s=100, label='Setosa', edgecolors='k')
    plt.scatter(X[other_mask, 0], X[other_mask, 1], 
                c='red', marker='s', s=100, label='Others', edgecolors='k')
    
    # Create grid for decision boundary
    x1_min, x1_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    x2_min, x2_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    
    # Plot decision boundary: w1*x1 + w2*x2 + b = 0
    # Rearrange to x2 = -(w1*x1 + b) / w2
    if abs(w[1]) > 1e-10:  # Check if not vertical
        x1_line = np.array([x1_min, x1_max])
        x2_line = -(w[0] * x1_line + b) / w[1]
        plt.plot(x1_line, x2_line, 'k-', linewidth=2, label='Decision boundary')
        
        # Plot margins: w1*x1 + w2*x2 + b = ±1
        x2_margin_plus = -(w[0] * x1_line + b - 1) / w[1]
        x2_margin_minus = -(w[0] * x1_line + b + 1) / w[1]
        plt.plot(x1_line, x2_margin_plus, 'k--', linewidth=1.5, label='Margin')
        plt.plot(x1_line, x2_margin_minus, 'k--', linewidth=1.5)
    
    plt.xlabel('Petal Length (cm)', fontsize=12)
    plt.ylabel('Petal Width (cm)', fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    
    return plt

# Simple gradient-based optimization for SVM
def train_svm(X, y, learning_rate=0.01, epochs=1000, C=1.0):
    """
    Train SVM using gradient descent
    Minimize: 0.5 * ||w||^2 + C * sum(max(0, 1 - y_i(w·x_i + b)))
    """
    n_samples, n_features = X.shape
    w = np.random.randn(n_features) * 0.01
    b = 0
    
    for epoch in range(epochs):
        # Compute margins
        margins = y * (X @ w + b)
        
        # Gradient for w
        dw = w.copy()
        
        # Add contribution from misclassified or margin-violating points
        for i in range(n_samples):
            if margins[i] < 1:
                dw -= C * y[i] * X[i]
        
        # Gradient for b
        db = 0
        for i in range(n_samples):
            if margins[i] < 1:
                db -= C * y[i]
        
        # Update parameters
        w -= learning_rate * dw
        b -= learning_rate * db
    
    return w, b