N , c1, c2 = input().split()
S = str(input())
# 下処理.
N = int(N)

# c1で無ければc2を出力
for c in S:
    if c != c1:
        print(c2, end="")
        continue
    print(c, end="")