N = int(input())
result = ["-"] * N

if N % 2 == 0:
    result[N//2] = "="
    result[N//2-1] = "="
else:
    result[N//2] = "="

print("".join(result))
