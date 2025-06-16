N, Q = map(int, input().split())
X = list(map(int, input().split()))
box_num = [0]* N
ans = []
for x in X:
    if x > 0:
        box_num[x-1] += 1
        ans.append(x)
    elif x == 0:
        min_idx = box_num.index(min(box_num))
        box_num[min_idx] += 1
        ans.append(min_idx+1)

print(*ans)


            
    
