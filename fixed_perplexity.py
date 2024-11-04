import numpy as np
from math import dist


# Function to calculate Euclidean distance
def calculate_euclidean_dist(datapoints, centroid, round_=False):
    result = dist(datapoints, centroid)
    return result if not round_ else round(result, 2)


# Function to initialize an empty cluster with correct dimensionality
def initialize_empty_cluster(dimension):
    return np.empty((0, dimension))


# Function to calculate centroid, handling empty clusters
def calculate_centroid(cluster, previous_centroid):
    if len(cluster) > 0:
        return np.mean(cluster, axis=0)
    else:
        return previous_centroid


# Initial centroids
centroid_1 = np.array([0, 0])
centroid_2 = np.array([2, 2])

# Input number of datapoints
n = int(input())

# Input datapoints
datapoints = []
for i in range(n):
    x = [float(x) for x in input().split()]
    datapoints.append(x)

# Convert datapoints to numpy array for efficiency
datapoints = np.array(datapoints)

# Initialize empty clusters
closter_1 = initialize_empty_cluster(len(centroid_1))
closter_2 = initialize_empty_cluster(len(centroid_2))

# Assign datapoints to clusters
for dp in datapoints:
    res_1 = calculate_euclidean_dist(dp, centroid_1, round_=True)
    res_2 = calculate_euclidean_dist(dp, centroid_2, round_=True)
    if res_1 <= res_2:  # Use <= instead of string comparison
        closter_1 = np.vstack([closter_1, dp])
    else:
        closter_2 = np.vstack([closter_2, dp])

# Calculate new centroids
centroid_1 = calculate_centroid(closter_1, centroid_1)
centroid_2 = calculate_centroid(closter_2, centroid_2)

# Print results
print(centroid_1.round(2))
print(centroid_2.round(2))
