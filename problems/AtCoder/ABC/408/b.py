N = int(input())
A = list(map(int, input().split()))

A_set = set(A)
result = sorted(list(A_set))
print(len(result))
print(*result)