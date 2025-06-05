def value_check(set_A: set, M: int) -> bool:
    if len(set_A) != M:
        return False
    
    for value in range(1, M+1):
        if not value in set_A:
            return False
    return True

N, M = map(int, input().split())
A = list(map(int, input().split()))

set_A = set(A)
cnt = 0
while True:
    if not value_check(set_A, M):
        print(cnt)
        exit()

    A.pop()
    set_A = set(A)
    cnt += 1
        