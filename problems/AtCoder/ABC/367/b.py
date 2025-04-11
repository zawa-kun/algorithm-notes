X = list(input())

zero_idx = len(X)
for i in range(1, len(X) - X.index('.')):
    if X[-(i)] == '0':
        zero_idx = len(X) - i
    else:
        break
result = X[:zero_idx]

# 整数の場合，小数点を取り除く
if result[-1] == '.':
    result = X[:zero_idx-1]

for s in result:
    print(s, end='')