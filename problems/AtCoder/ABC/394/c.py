S = str(input())

len_S = len(S)
if len_S < 2:
    print(S)
    exit()
S = list(S)

i = 0
while i < len_S-1:
    if S[i] == "W" and S[i+1] == "A":
        S[i] = "A"
        S[i+1] = "C"
        i = max(0, i-1)
    else:
        i += 1


for s in S:
    print(s, end="")