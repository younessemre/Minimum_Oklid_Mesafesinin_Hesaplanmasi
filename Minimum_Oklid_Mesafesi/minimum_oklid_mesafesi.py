import math

def euclideanDistance(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

points = [(0, 0), (1, 1), (2, 3), (4, 6), (9, 3)]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

minimum_distance = min(distances)


print("Nokta grupları arasındaki mesafeler: ", distances)
print("En kısa mesafe: ", minimum_distance)
