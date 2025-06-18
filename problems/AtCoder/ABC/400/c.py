N = int(input())
ans = 0

# aが奇数のとき: X = 2 * b^2
max_b = int((N // 2) ** 0.5)
ans += max_b

# aが偶数のとき: X = 4 * b^2
max_c = int((N // 4) ** 0.5)
ans += max_c

print(ans)