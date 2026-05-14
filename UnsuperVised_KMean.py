import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

# Generate data
X, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.40, random_state=0)

# Train-test split
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Train KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_train)

# Predictions
y_train_pred = kmeans.predict(X_train)
y_test_pred = kmeans.predict(X_test)

# Plot training data
plt.scatter(X_train[:, 0], X_train[:, 1],
            c=y_train_pred, s=50, cmap='viridis', label="Train")

# Plot test data
plt.scatter(X_test[:, 0], X_test[:, 1],
            c=y_test_pred, s=50, cmap='coolwarm', marker='x', label="Test")

# Plot centroids
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1],
            c='red', s=200, alpha=0.75,
            marker='X', label='Centroids')

plt.title("K-Means Clustering")
plt.legend()
plt.show()
