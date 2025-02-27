N, M = map(int,input().split())# N: Aの最大値, M: Aの要素数.
A = list(map(int, input().split())) # Aの要素を格納するリスト.
# N, M = 10, 3
# A = [3, 9, 2]

A.sort() # Aを昇順にソート.
beside_A = [] # Aの要素と一致しないものを格納するリスト.

while len(A) > 0: # Aの要素を全て見るまでループ.
    for i in range(1, N+1): # 1からNまでの数を見る.
        if len(A) == 0: 
            beside_A.append(i) # Aが空の場合は全ての要素をbeside_Aに格納する.
        elif i != A[0]: 
            beside_A.append(i) # Aの要素と一致しない場合はbeside_Aに格納する.
        elif i == A[0]: 
            A.pop(0)           # Aの要素と一致する場合はpopする.
        
        if i > N: break # iがNになったらループを抜ける.

# 出力.
print(len(beside_A))
for num in beside_A:
    print(num, end=" ")