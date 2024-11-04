import numpy as np

def calculate_euclidean_dist(point1, point2, round_=False):
    squared_dist = sum((a - b) ** 2 for a, b in zip(point1, point2))
    result = squared_dist ** 0.5
    return round(result, 2) if round_ else result

def mean(points):
    return [sum(coord) / len(points) for coord in zip(*points)]

centroids = {
    1: [0, 0],
    2: [2, 2]
}

n = int(input())

datapoints = []
for _ in range(n):
    x = [float(x) for x in input().split()]
    datapoints.append(x)

cluster_1 = []
cluster_2 = []

for dp in datapoints:
    res_1 = calculate_euclidean_dist(dp, centroids[1], round_=True)
    res_2 = calculate_euclidean_dist(dp, centroids[2], round_=True)
    if res_1 <= res_2:
        cluster_1.append(dp)
    else:
        cluster_2.append(dp)

centroids[1] = mean(cluster_1) if cluster_1 else centroids[1]
centroids[2] = mean(cluster_2) if cluster_2 else centroids[2]

print(np.array(centroids[1]).round(2))
print(np.array(centroids[2]).round(2))
