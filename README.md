# K-Means Clustering with Python

This project is a simple look at how K-Means clustering can find groups in data without being told which group each point belongs to.

I used Scikit-learn's `make_blobs()` function to create a dataset with several naturally separated groups. The generated points are then passed to a K-Means model, which tries to discover the four clusters on its own.

What makes this project interesting is that there are no target labels given to the K-Means algorithm during training. Instead, the algorithm looks at the positions of the points and organizes them into clusters based on their similarity.

The results are visualized with Matplotlib so the different groups can be seen directly on the graph. The center of each cluster is also displayed, making it easier to understand what K-Means has found.

### A Simple Experiment

The project follows a straightforward process:

```text
Generate Data
      ↓
Visualize the Points
      ↓
Apply K-Means
      ↓
Predict Cluster Labels
      ↓
Find Cluster Centers
      ↓
Visualize the Result
```

### Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

### What I Learned

This project helped me understand the basic idea behind unsupervised learning and how clustering can be used to discover patterns in data.

I also practiced working with synthetic datasets, training a K-Means model, obtaining cluster labels, and plotting cluster centers.

### Running the Project

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Then run:

```bash
python kmeans_clustering.py
```

### Why K-Means?

K-Means is a useful starting point for understanding clustering because the result is easy to visualize. In this project, the algorithm gets only the data points and the number of clusters, then tries to find the best grouping.

This small experiment was a good way to see unsupervised learning working visually rather than only reading about it.
