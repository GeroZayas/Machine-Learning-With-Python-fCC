import numpy as np
from math import dist


def calculate_euclidean_dist(datapoints, centroid, round_=False):
    result = dist(datapoints, centroid)
    return result if not round_ else round(result, 2)

centroids = {
    1: [0,0],
    2: [2,2]
}

n = int(input())

datapoints = []
for i in range(n):
    x = [float(x) for x in input().split()]
    datapoints.append(x)

closter_1 = []
closter_2 = []

for i, dp in enumerate(datapoints):
    res_1 = calculate_euclidean_dist(dp, centroids[1], round_=True)
    res_2 = calculate_euclidean_dist(dp, centroids[2], round_=True)
    r = min(res_1,res_2)
    if str(r) in str(res_1) or res_1 == res_2:
        closter_1.append(dp)
    else:
        closter_2.append(dp)

for closter in [closter_1, closter_2]:
    if closter == []:
        closter = None

new_centroid_1 = np.array(closter_1)
new_centroid_2 = np.array(closter_2)

centroids[0] = np.mean(new_centroid_1, axis=0)
centroids[1] = np.mean(new_centroid_2, axis=0)

print(centroids[0].round(2))
print(centroids[1].round(2))