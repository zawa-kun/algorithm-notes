N = int(input())
G = [['.']*N for _ in range(N)]

for i in range(N):
    j = N-1-i
    if(i > j): continue

    c = '#'
    if i%2 == 1: c = '.'
    for x in range(i, j+1):
        for y in range(i, j+1):
            G[x][y] = c

for row in G:
    print(''.join(row))