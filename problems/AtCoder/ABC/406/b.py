N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 1 # 計算結果

for value in A:
    result *= value
    if len(str(result)) >= K + 1:
        result = 1

print(result)