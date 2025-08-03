import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.cluster import KMeans

file_path = "machine_learning/03.statistics/05.k-means-clustering/00.data/02.example.csv"
data = pd.read_csv(file_path)

# plt.scatter(data["Satisfaction"], data["Loyalty"])
# plt.xlabel("Satisfaction")
# plt.ylabel("Loyalty")
# plt.show()

x = data.copy()
kmeans = KMeans(2)
kmeans.fit(x)
clusters = x.copy()
clusters["Cluster_pred"] = kmeans.fit_predict(x)

# plt.scatter(
#     clusters["Satisfaction"], 
#     clusters["Loyalty"],
#     c=clusters["Cluster_pred"],
#     cmap="rainbow"
# )
# plt.xlabel("Satisfaction")
# plt.ylabel("Loyalty")
# plt.show()

"""
Standardize the variable
"""
x_scaled = preprocessing.scale(x)

"""
Elbow Method
"""
# wcss = []
# for i in range(1, 10):
#     kmeans = KMeans(i)
#     kmeans.fit(x_scaled)
#     wcss.append(kmeans.inertia_)

# plt.plot(range(1,10), wcss)
# plt.xlabel("Number of clusters")
# plt.ylabel("WCSS")
# plt.show()

"""
Eplore clustering solutions and select the number of 
clusters
Try number of clusters observed from the elbow plot
"""
kmeans_new = KMeans(5)
kmeans_new.fit(x_scaled)
clusters_new = x.copy()
clusters_new["cluster_pred"] = kmeans_new.fit_predict(x_scaled)

plt.scatter(
    clusters_new["Satisfaction"], 
    clusters_new["Loyalty"],
    c=clusters_new["cluster_pred"],
    cmap="rainbow"
)
plt.xlabel("Satisfaction")
plt.ylabel("Loyalty")
plt.show()