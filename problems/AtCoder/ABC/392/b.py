# １からNまで出力していき、もし、Aの要素と一致する下図の時は出力しない.

# N, M = map(int,input().split())# N: Aの最大値, M: Aの要素数.
# A = [map(int, input().split())]
beside_A = [] # Aの要素と一致しないものを格納するリスト.
N, M = 10, 3
A = [3, 9, 2]

# Aの要素と一致しないものをbeside_Aに格納.
for i in range(1, N+1):
    for j in range(M):
        if i != A[j]:
            beside_A.append(i)
            break

#一致しないモノの最大値を出力.
print(beside_A[-1])
#一致しないものを出力.
for num in beside_A:
    print(num, end=" ")