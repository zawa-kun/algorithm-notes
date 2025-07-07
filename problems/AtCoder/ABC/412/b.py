S = str(input())
T = str(input())

flag = True
for i in range(1, len(S)):
    if S[i].isupper():
        if S[i-1] not in T:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
