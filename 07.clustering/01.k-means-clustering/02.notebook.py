import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

file_path = "data_science/03.statistics/05.k-means-clustering/00.data/01.country_clusters.csv"
data = pd.read_csv(file_path)

"""
Plot the data
"""
plt.scatter(data["Longitude"], data["Latitude"])
plt.xlim(-180,180)
plt.ylim(-90,90)
# plt.show()

"""
Select the features
"""
x = data.iloc[:,1:3]
kmeans = KMeans(3)
kmeans.fit(x)

identified_clusters = kmeans.fit_predict(x)
data_with_clusters = data.copy()
data_with_clusters["Cluster"] = identified_clusters

plt.scatter(
    data_with_clusters["Longitude"], 
    data_with_clusters["Latitude"],
    c=data_with_clusters["Cluster"], 
    cmap="rainbow"
)
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show()