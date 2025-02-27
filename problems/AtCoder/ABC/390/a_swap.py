#390-Aの入れ替えの総当たりで解いた場合
a = list(map(int, input().split()))

for i in range(4):
    list = a.copy()
    list[i], list[i+1] = list[i+1], list[i]
    if list == [1, 2, 3, 4, 5]:
        print("Yes")
        exit()

print("No")