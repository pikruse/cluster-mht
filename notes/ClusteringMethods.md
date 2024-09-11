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