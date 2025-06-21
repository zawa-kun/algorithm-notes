N, Q = map(int, input().split())
A = list(map(int, input().split()))
for i in range(len(A)):
    A[i] -= 1

cnt = 0 
print(A)
M = [0] * N
for idx in A: # 反転させるクエリ
    print(idx, "のクエリ")
    if M[idx] == 0:
        M[idx] = 1
    elif M[idx] == 1:
        M[idx] =0
    print(*M)

    if idx != 0: 
        l1 = M[idx-1] # 一番左の時は左側見れない
    if idx != N-1:
        r1 = M[idx+1] # 一番右の時は右側見れない
    
    # 左右白の時は一つも増えない
    if A[idx-1] == 0 and A[idx+1] == 0:
        cnt += 1
        print(cnt)
        continue

    if idx >= 2:
        l2 = M[idx-2]
    
    if N - idx - 1>= 2:
        r2 = M[idx+2]

    
    if (A[idx-1] and A[idx-2]) and (A[idx+1] and A[idx+2]):
        cnt -= 1
    elif (A[idx-1] and A[idx-2] == 0) or (A[idx+1] and A[idx+2] == 0):
        cnt += 0 # 変化しない
    else:
        cnt += 1

    print(cnt)


    
    