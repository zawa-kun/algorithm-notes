N = int(input())
A = list(map(int, input().split()))

cnts = [0]*(N+1)
for i in range(N+1):
    for num in A:
        if num >= i:
            cnts[i] += 1
# print(cnts)
max = -1
for i, cnt in enumerate(cnts):
    if i <= cnt:
        max = i
print(max)