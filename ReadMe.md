# The MHT Cluster Project
We are clustering sequences from a multiple sequence alignment (MSA) based on amino acids representing the binding sites. The we use the following procedure:

## 1. Identify Binding Sites:
Manually identify binding site regions from the MSA data. Create a dataframe containing only sequences names and binding site residues.

## 2. Convert the Extracted Sites into Feature Vectors:
For each sequence, create a feature vector that corresponds to the amino acids at the binding site positions. Describe features with a mix of ordinal and one-hot encoding methods. Features are from the [IMGT website](https://www.imgt.org/IMGTeducation/Aide-memoire/_UK/aminoacids/IMGTclasses.html).

## 3. Clustering:
Using [k-means clustering and hierarchical clustering](notes/ClusteringMethods.md), group similar binding sites with each other. Plot clusters in 2-D space with dimension reduction methods and compare their distinctness using the [silhouette score](https://medium.com/@hazallgultekin/what-is-silhouette-score-f428fb39bf9a).

## 4. Validation of Clusters:
Evaluate the biological relevance of the clusters by mapping back the clustered sequences to their original MSA and checking for conservation, structural relevance, or known functional motifs.