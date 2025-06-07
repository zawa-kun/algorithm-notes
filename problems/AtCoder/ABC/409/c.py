N, L = map(int, input().split())
distances = list(map(int, input().split()))

if L % 3 != 0:
    print(0)
    exit()

position = [0] * L
position[0] += 1 # 点１を記録
p = 0
for distance in distances:
    p += distance
    if p >= L:
        p %= L
    position[p] += 1

# print(position)
total = 0
for i in range(L // 3):
    # print(i)
    if position[i] > 0: # 座標iに点が存在するとき
        if position[i+L//3] > 0 and position[i+(2*L//3)]:
            total += position[i] * position[i+L//3] * position[i+(2*L//3)]

print(total)