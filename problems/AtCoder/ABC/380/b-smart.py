S = input()
ans= []
cnt = 0
for i in range(1, len(S)):
  if S[i] == "-":
    cnt += 1
  else:
    ans.append(cnt)
    cnt = 0
print(*ans)