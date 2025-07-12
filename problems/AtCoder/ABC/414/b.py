N = int(input())
len = 0
ans = []
for _ in range(N):
    c, l_str = input().split()
    l = int(l_str)
    
    len += l
    if len > 100:
        print("Too Long")
        exit()
    else:
        ans.append(c*l)

print("".join(map(str, ans)))
        