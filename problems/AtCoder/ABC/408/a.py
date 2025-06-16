N, S = map(int, input().split())
T = list(map(int, input().split()))

if T[0] > S+0.5:
    print("No")
    exit()

for i in range(N-1):
    if T[i+1]-T[i] > S+0.5:
        print("No")
        exit()
print("Yes")