import copy

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = copy.deepcopy(A)

for b in B:
    for i in range(len(A)):
        if A[i] == b:
            A.pop(i)
            break
        elif A[i] > b:
            break

print(" ".join(map(str, A)))