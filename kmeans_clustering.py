
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

sns.set()

x, y_true = make_blobs(
    n_samples=400,
    centers=4,
    cluster_std=0.60,
    random_state=0
)

plt.scatter(
    x[:, 0],
    x[:, 1],
    s=20
)

plt.show()

print(x[0])
print(y_true)

kmeans = KMeans(
    n_clusters=4
)

kmeans.fit(x)

y_kmeans = kmeans.predict(x)

output = kmeans.predict(x)

plt.scatter(
    x[:, 0],
    x[:, 1],
    c=output,
    s=20,
    cmap="viridis"
)

plt.show()

centers = kmeans.cluster_centers_

plt.scatter(
    x[:, 0],
    x[:, 1],
    c=y_kmeans,
    s=20,
    cmap="viridis"
)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    s=200,
    c="red",
    marker="."
)

plt.show()

print(centers)





