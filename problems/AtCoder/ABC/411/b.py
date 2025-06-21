N = int(input())
D = list(map(int, input().split()))

if N == 2:
    print(D[0])
    exit()


# D_abs = [D[0]]
# sum = D[0]
# for i in range(1, N-1):
#     sum += D[i]
#     D_abs.append(sum)

# print(*D_abs)
# for i in range(N - 1):
#     ans = []
#     for j in range(i+1, N-1):
#         ans.append(D_abs[j] - D_abs[i])
#     print(*ans)

for i in range(N-1):
    ans = []
    total = 0
    for j in range(i, N-1):
        total += D[j]
        ans.append(total)
    
    print(*ans)