import numpy as np
from math import dist


def calculate_euclidean_dist(datapoints, centroid, round_=False):
    result = dist(datapoints, centroid)
    return result if not round_ else round(result, 2)


centroid_1 = [0, 0]
centroid_2 = [2, 2]

n = int(input())

datapoints = []
for i in range(n):
    x = [float(x) for x in input().split()]
    datapoints.append(x)

closter_1 = []
closter_2 = []

for i, dp in enumerate(datapoints):
    res_1 = calculate_euclidean_dist(dp, centroid_1, round_=True)
    res_2 = calculate_euclidean_dist(dp, centroid_2, round_=True)
    r = min(res_1, res_2)
    if str(r) in str(res_1) or res_1 == res_2:
        closter_1.append(dp)
    else:
        closter_2.append(dp)

for closter in [closter_1, closter_2]:
    if len(closter) == 0:
        closter.append([])

new_centroid_1 = np.array(closter_1)
new_centroid_2 = np.array(closter_2)

centroid_1 = np.mean(new_centroid_1, axis=0)
centroid_2 = np.mean(new_centroid_2, axis=0)

print(centroid_1.round(2))
print(centroid_2.round(2))
