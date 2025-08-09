S = list(input())

t_idxs = []
for i in range(len(S)):
    if S[i] == "t":
        t_idxs.append(i)

ans = 0
for t1 in range(len(t_idxs)):
    t_cnt = 2
    for t2 in range(t1+1, len(t_idxs)):
        t_length = abs(t_idxs[t2] - t_idxs[t1]) + 1
        if t_length >= 3: #長さ３以上であれば
            if (t_cnt - 2) / (t_length - 2) > ans:
                ans = (t_cnt - 2) / (t_length - 2)
        t_cnt += 1

print(ans)

    