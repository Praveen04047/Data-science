
# Sample k-Means clustering in Python
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

# Load or create your dataset
data = pd.read_csv("your_dataset.csv")

# Extract features
X = data.iloc[:, :4]

# Perform k-Means clustering with k=3
kmeans_model = KMeans(n_clusters=3, random_state=123)
kmeans_result = kmeans_model.fit_predict(X)

# Display the cluster assignments
print("Cluster Assignments:")
print(kmeans_result)

# Display the cluster centers
print("Cluster Centers:")
print(kmeans_model.cluster_centers_)
