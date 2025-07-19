def solve():
    N = int(input())
    S = input() # S[i]: 状態iの状態

    state = 0
    drags = list(range(N)) # idx ベースで管理
    while drags:
        i = 0
        added_any = False
        
        while i < len(drags):
            test_state =  state + 2**(drags[i])
            if S[test_state-1] != "1": # 危険でなければ
                state = test_state # 状態更新
                drags.pop(i)
                added_any = True
            else:
                i += 1 # 次の薬へ
        
        if not added_any:
            print("No")
            return


    print("Yes")
    return        

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()