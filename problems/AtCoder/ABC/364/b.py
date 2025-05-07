H, W = map(int, input().split())
S = list(map(int, input().split()))
C = [list(input()) for _ in range(H)]
X = str(input())

# インデックスに合わせる
S[0] -= 1
S[1] -= 1 

for x in X:
    Sx = S[0]
    Sy = S[1]
    if x == "L":
        Sy -= 1
    elif x == "R":
        Sy += 1
    elif x == "U":
        Sx -= 1
    elif x == "D":
        Sx += 1
    
    if (0 <= Sx and Sx <= H-1 and 0 <= Sy and Sy <= W-1 and C[Sx][Sy] == "."):
        S[0] = Sx
        S[1] = Sy

S[0] += 1
S[1] += 1
print(*S)


