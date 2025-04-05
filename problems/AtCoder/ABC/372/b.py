M = int(input())

for i in range(20):
    if 3 ** i  == M:
        print(1)
        print(i)
        exit()

    if 3 ** i  > M:
        A = []
        A.append(i-1)
        while len(A) < i:
            A_idx = 0
            M -= 3 ** A[A_idx]
            # 3^i をMから引いていきMが負の数になるときのiのi-1をAにアペンドし、繰り返していき、
            # もし配列の長さがiを上回ったらこのnに満たすnは存在しないことになる。
            for A_kouho in range(i):
                if M - 3 ** A_kouho == 0:
                    A.append(A_kouho)
                    # output result
                    print(i)
                    print(*A, sep=' ') 
                elif M - 3 ** A_kouho < 0 :
                    A.append(A_kouho)
            A_idx += 1