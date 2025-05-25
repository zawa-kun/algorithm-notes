X, Y = map(int, input().split())

all = 6 * 6

x_pat = []
y_pat = []

for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= X:
            x_pat.append((i,j))

        if abs(i - j) >= Y:
            y_pat.append((i,j))
all_set = set(x_pat + y_pat)


print(len(all_set) / all)