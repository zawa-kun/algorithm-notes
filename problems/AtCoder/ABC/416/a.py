N, L, R = map(int, input().split())
S = list(input())

# インデックスを整える
L -= 1
R -= 1

for i in range(L, R+1):
    # print(i, ":", S[i])
    if S[i] != "o":
        print("No")
        exit()

print("Yes")