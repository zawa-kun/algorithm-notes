A, B = map(int, input().split())

ans = A / B

sa = A / B - A // B

if sa >= 0.5:
    print(A//B + 1)
else:
    print(A//B)