M = int(input())

for i in range(20):
    if 3 ** i  == M:
        print(1)
        print(i)
        exit()
    
    if 3 ** i  > M:
        A = [0] * i
        A_idx = 0
        # A[A_idx] = i-1
        nokori = M
        while A_idx < i and nokori > 0:
            for A_kouho in range(i):
                if nokori - 3 ** A_kouho == 0:
                    A[A_idx] = A_kouho
                    # output result
                    print(i)
                    A = A[:A_idx+1]
                    print(*A, sep=' ')
                    exit()
                elif nokori - 3 ** A_kouho > 0 :
                    A[A_idx] = A_kouho

            nokori -= 3 ** A[A_idx]
            A_idx += 1

    # if 3 ** i  > M:
    #     A = [0] * i
    #     A_idx = 0
    #     A[A_idx] = i-1
    #     nokori = M
    #     # nokori = M - 3 ** i-1 
    #     while A_idx < i - 1 and nokori > 0:
            
    #         nokori -= 3 ** A[A_idx]
    #         for A_kouho in range(i):
    #             if nokori - 3 ** A_kouho == 0:
    #                 A[A_idx+1] = A_kouho
    #                 # output result
    #                 print(i)
    #                 print(*A, sep=' ')
    #                 exit()
    #             elif nokori - 3 ** A_kouho > 0 :
    #                 A[A_idx+1] = A_kouho

    #         A_idx += 1
            