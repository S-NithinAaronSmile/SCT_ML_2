import pandas as pd

# Load the dataset
data = pd.read_csv("Mall_Customers.csv")

# Look at the relevant columns
print(data[["Annual Income (k$)", "Spending Score (1-100)"]].head())

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# Try K from 1 to 10, record how tight the clusters are each time
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertia.append(km.inertia_)

# Plot it
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia (tightness of clusters)")
plt.title("Elbow Method")
plt.savefig("elbow_plot.png")
print("Elbow plot saved as elbow_plot.png")
# Build the final model with K=5 clusters
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
data["Cluster"] = kmeans.fit_predict(X)

# Show a few rows with their assigned cluster
print(data[["Annual Income (k$)", "Spending Score (1-100)", "Cluster"]].head(10))
# Visualize the clusters
plt.figure()
colors = ['red', 'blue', 'green', 'purple', 'orange']

for cluster_num in range(5):
    cluster_points = data[data["Cluster"] == cluster_num]
    plt.scatter(cluster_points["Annual Income (k$)"], 
                cluster_points["Spending Score (1-100)"], 
                c=colors[cluster_num], 
                label=f"Cluster {cluster_num}")

# Mark the center of each cluster
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='black', marker='X', s=200, label='Centroids')

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segments")
plt.legend()
plt.savefig("customer_clusters.png")
print("Cluster plot saved as customer_clusters.png")