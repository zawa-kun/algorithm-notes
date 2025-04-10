N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
    A.sort(reverse=True)
    if A[1] <= 0:
        print(cnt)
        exit() 
    A[0] -= 1
    A[1] -= 1
    cnt += 1
