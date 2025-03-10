N, D = map(int, input().split())
S = str(input())

emp = S.count(".") # 最初の空き箱の数.

# 最終的な空き箱の数
# (最初の空き箱) + (食べる日数)
print(emp + D)