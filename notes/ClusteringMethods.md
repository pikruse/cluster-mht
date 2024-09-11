# Clustering Methods
An overview of k-means and hierarchical clustering in layman's terms.

**Definition:** *Centroid* - The center point of a shape/object, also known as the center of mass. Calculated as the arithmetic mean of all points in a shape's surface.

## K-Means Clustering
1. Choose a *k* value, representing the number of clusters you will have
2. Randomly initialize *k* points, representing the centroid for each cluster
3. Assign observations in your data to one of the clusters. The centroid with the shortest distance to each point will be the group that it belongs to.
4. Re-initialize the *k* centroids as the arithmetic mean for each group. 
5. Re-measure the distance between points and centroids, and switch their group if the closest centroid to a point changes.
6. Repeat steps 4-5 until group membership is stable (points are not switching)

## Hierarchical Clustering
There are two types of hierarchical clustering:
* *Agglomerative:* each object starts as its own cluster, and clusters are merged until a single cluster remains

* *Divisive:* all objects start in the same cluster, and clusters are divided until each point has a unique cluster.

We will focus on *agglomerative* clustering for the analysis.

**Agglomerative clustering steps:**
1. Compute the proximity/dissimilarity/distance matrix with a chosen distance metric
2. Assign each data point its own cluster
3. Merge clusters based on similarity metric (closest clusters are grouped together)
    * Several similarity metrics exist:
        1. Min (Single) Linkage - finds the minimum distance between points in clusters
        2. Max (Complete) Linkage - finds the maximum distance between points in clusters
        3. Centroid Linkage - finds the distance between cluster centroids
        4. Average Linkage - finds the average distance of all  points in clusters, compared pairwise
4. Repeat Step 3 until one cluster exists.
