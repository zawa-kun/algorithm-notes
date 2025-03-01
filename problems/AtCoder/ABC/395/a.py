N = int(input())
A = [int(i) for i in input().split()]

for i in range(N-1):
    if A[i] >= A[i+1]:
        print("No")
        exit()

print("Yes")