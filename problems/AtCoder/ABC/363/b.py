N, T, P = map(int,input().split())
L = list(map(int, input().split()))
L.sort()

cnt = 0
day = 0
while True:
    T_index = len(L)
    for i in range(len(L)): # Lの全要素を調べる
        if L[i] + day >= T:
            T_index = i
            break
    cnt += len(L) - T_index # 値T以上の要素数を取得
    del L[T_index:]
    if cnt >= P:
        break
    day += 1
    
print(day)