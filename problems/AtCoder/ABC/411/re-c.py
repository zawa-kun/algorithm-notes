N, Q = map(int, input().split())
Querys = list(map(int, input().split()))

A = [0] * (N+2)
ans = 0
for idx in Querys:
    if A[idx] == 0:
        A[idx] = 1 # 塗り替え 
        if A[idx-1] == 0 and A[idx+1] == 0:
            ans += 1
        elif A[idx-1] == 1 and A[idx+1] == 1:
            ans -= 1
        
    elif A[idx] == 1:
        A[idx] = 0
        if A[idx-1] == 1 and A[idx+1] == 1:
            ans += 1
        elif A[idx-1] == 0 and A[idx+1] == 0:
            ans -= 1
    print(ans)
