import copy

N = int(input())
A = list(map(int, input().split()))
origin = copy.deepcopy(A)
A.sort()
ans = origin.index(A[-2]) + 1

print(ans)