import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.metrics import silhouette_samples, silhouette_score


def plot_silhouette(X, labels, title="Silhouette Diagram", figsize=(10, 6), cmap="tab10"):
    """
    Plot a silhouette diagram for clustered data.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Feature matrix used for clustering.
    labels : array-like of shape (n_samples,)
        Cluster labels for each sample (integers starting at 0).
    title : str, optional
        Title of the plot. Default is "Silhouette Diagram".
    figsize : tuple, optional
        Figure size as (width, height). Default is (10, 6).
    cmap : str, optional
        Matplotlib colormap name for cluster colors. Default is "tab10".

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure object.
    ax : matplotlib.axes.Axes
        The axes object.
    avg_score : float
        The mean silhouette score across all samples.

    Example
    -------
    >>> from sklearn.datasets import make_blobs
    >>> from sklearn.cluster import KMeans
    >>> X, _ = make_blobs(n_samples=300, centers=4, random_state=42)
    >>> labels = KMeans(n_clusters=4, random_state=42).fit_predict(X)
    >>> fig, ax, score = plot_silhouette(X, labels)
    >>> print(f"Average silhouette score: {score:.3f}")
    >>> plt.show()
    """
    X = np.array(X)
    labels = np.array(labels)

    unique_clusters = np.unique(labels)
    n_clusters = len(unique_clusters)

    if n_clusters < 2:
        raise ValueError("Silhouette score requires at least 2 clusters.")

    # Compute silhouette scores
    sample_scores = silhouette_samples(X, labels)
    avg_score = silhouette_score(X, labels)

    fig, ax = plt.subplots(figsize=figsize)
    colormap = cm.get_cmap(cmap, n_clusters)

    y_lower = 10  # starting y position for the first cluster bar

    for i, cluster_id in enumerate(unique_clusters):
        cluster_scores = np.sort(sample_scores[labels == cluster_id])
        cluster_size = len(cluster_scores)
        y_upper = y_lower + cluster_size

        color = colormap(i)
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            cluster_scores,
            facecolor=color,
            edgecolor=color,
            alpha=0.85,
        )

        # Label cluster in the middle of its bar
        ax.text(
            -0.05,
            y_lower + cluster_size / 2,
            str(cluster_id),
            ha="right",
            va="center",
            fontsize=10,
            fontweight="bold",
        )

        y_lower = y_upper + 10  # gap between clusters

    # Average score vertical line
    ax.axvline(x=avg_score, color="red", linestyle="--", linewidth=1.5,
               label=f"Avg score: {avg_score:.3f}")

    # Formatting
    ax.set_xlabel("Silhouette Coefficient", fontsize=12)
    ax.set_ylabel("Cluster", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_yticks([])  # hide y-axis ticks (clusters are labeled manually)
    # ax.set_xlim([-0.1, 1.0])
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(axis="x", linestyle=":", alpha=0.5)

    plt.tight_layout()
    return fig, ax, avg_score


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    from sklearn.cluster import KMeans

    # Generate sample data with 4 natural clusters
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)

    # Fit KMeans
    kmeans = KMeans(n_clusters=4, random_state=42, n_init="auto")
    labels = kmeans.fit_predict(X)

    fig, ax, score = plot_silhouette(X, labels, title="KMeans Silhouette Diagram (k=4)")
    print(f"Average silhouette score: {score:.3f}")
    plt.show()