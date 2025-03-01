x = int(input())
ans = 0
count = 0 # グリッド中のxの数.

for i in range(1,10):
    for j in range(1,10):
        ans += i*j
        if x == i*j:
            count += 1

if count:
    print(ans - x*count)
else:
    print(ans)