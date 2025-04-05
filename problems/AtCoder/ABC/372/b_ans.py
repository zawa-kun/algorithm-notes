M = int(input())
A = []
for k in range(11):
    A += [k] * (M % 3)
    M //= 3
print(len(A))
print(*A)