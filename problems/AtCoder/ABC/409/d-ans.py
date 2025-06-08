def solve():
    N = int(input())
    S = input()
    l = -1
    # 隣を比べ、一個前の数字の方が大きい時、何文字目を記録
    # l文字目を決定
    for i in range(N - 1):
        if S[i] > S[i+1]:
            l = i
            break
    if l == -1:
        print(S)
        return
    # r文字目（最後の文字）を決定
    r = N
    for j in range(l + 1, N):
        if S[l] < S[j]:
            r = j
            break
    print(S[:l] + S[l + 1 : r] + S[l] + S[r:])

T = int(input())
for _ in range(T):
    solve()