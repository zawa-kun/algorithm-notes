L, R = map(int, input().split())


if L == 1 and R == 1:
    print('Invalid')
elif L == 1 and R == 0:
    print('Yes')
elif L == 0 and R == 1:
    print('No')