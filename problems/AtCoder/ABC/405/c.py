N = int(input())
A = list(map(int, input().split()))

sum = 0
for v in A:
    sum += v

result = 0
# 最後の要素の一個前まで計算
for i in range(len(A)-1):
    sum -= A[i]
    result += A[i]*sum

print(result)