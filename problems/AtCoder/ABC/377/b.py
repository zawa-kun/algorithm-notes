def check_square(S, i, j):
    for s in S[i]:
        if s == "#":
            return False
        
    for row in S:
        if row[j] == "#":
            return False
    return True

S = [str(input()) for _ in range(8)]

ans = 0

for i in range(8):
    for j in range(8):
        if check_square(S, i, j):
            ans += 1

print(ans)