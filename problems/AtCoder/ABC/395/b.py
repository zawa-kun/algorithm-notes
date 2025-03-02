N = int(input())

target = [["?"]*N for _ in range(N)]

for i in range(N):
    j = N - i - 1
    if i <= j:
        for x in range(i, j+1):
            for y in range(i, j+1):
                if i % 2 == 0:
                    target[x][y] = "#"
                else:
                    target[x][y] = "."

for row in target:
    print("".join(row))
            

