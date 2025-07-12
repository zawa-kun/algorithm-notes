N, M = map(int, input().split())
X = list(set(map(int, input().split())))

sorted_X = sorted(X)
print("sorted_X", sorted_X)
distances = []
for i in range(N-2):
    distances.append(sorted_X[i+1]-sorted_X[i])
print("distances:", distances)
sorted_distances = sorted(distances, reverse=True)
print(sorted_distances)
divide_area = [[0, 0] for _ in range(M-1)]
for i in range(M-1):
    for j, x in enumerate(distances):
        if x == sorted_distances[i]:
            divide_area[-i-1] = [j, j+1]
            break

print(divide_area)