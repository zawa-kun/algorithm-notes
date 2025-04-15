N, M = map(int, input().split())
result = 0

for i in range(M+1):
    result += N**i
    if result > 10 ** 9:
        print('inf')
        exit()

print(result)