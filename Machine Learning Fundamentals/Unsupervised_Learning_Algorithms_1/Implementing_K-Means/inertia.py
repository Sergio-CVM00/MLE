import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
samples = iris.data

num_clusters = list(range(1, 9))
inertias = []

for k in num_clusters:
  model = KMeans(n_clusters=k)
  model.fit(samples)
  inertias.append(model.inertia_)

plt.plot(num_clusters, inertias, '-o')

plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')

plt.show()

# Good clustering results in tight clusters, meaning that the samples in each cluster are bunched together. 
# How spread out the clusters are is measured by inertia. 
# Inertia is the distance from each sample to the centroid of its cluster. 
# The lower the inertia is, the better our model has done.