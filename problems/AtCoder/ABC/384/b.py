N, R = map(int, input().split())
DA = list(input().split() for _ in range(N)) 

for contest in range(N):
    if int(DA[contest][0]) == 1:     # Div.1のとき
        if 1600 <= R and R <= 2799:
            R += int(DA[contest][1])
    else:                            # Div.2のとき
        if 1200 <= R and R <= 2399:
            R += int(DA[contest][1])
print(R)