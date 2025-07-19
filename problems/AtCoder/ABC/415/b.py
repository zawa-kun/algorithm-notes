S = str(input())

x = 0
while x != len(S):
    cnt = 0
    output = []
    while cnt != 2 and x != len(S):
        if S[x] == "#":
            output.append(x+1)
            cnt += 1    
        x += 1
    print(*output, sep=",")