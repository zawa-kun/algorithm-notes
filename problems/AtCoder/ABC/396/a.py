N = int(input())
A = list(map(int, input().split()))

v = A[0]
count = 0
for i in range(1, N):
    if v == A[i]:
        if count == 0:
            count = 1
        count += 1
        if count >= 3:
            print("Yes")
            exit()
    else:
        count = 0
        v = A[i]

print("No")