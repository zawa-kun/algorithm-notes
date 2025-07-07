def solve():
    N = int(input())
    S = list(map(int, input().split()))

    # ドミノを一度も使っていない状態を記録
    used = [False] * N

    # 答え（並べるドミノの数）と現在のチェーンの最後尾のドミノのインデックス
    count = 1
    last_idx = 0 # start for idnex 0
    
    
    while True:
        # ゴール判定：　現在のドミノから直接ドミノNに移動到達できるか
        # S[last_idx] * 2 がドミノＮの大きさS[N-1]以上なら終了
        if S[last_idx] * 2 >= S[N-1]:
            count += 1
            break

        # 次のドミノを探す（貪欲法）
        # 条件を満たす中で、最大の大きさを持つドミノを探す
        next_idx = -1
        # ドミノ１とNを除く、未使用のドミノを探す
        for i in range(1, N - 1):
            if not used[i] and S[last_idx]*2 >= S[i]:
                #候補が見つかっていない、または今の候補より大きいものが見つかったら更新
                if next_idx == -1 or S[i] > S[next_idx]:
                    next_idx = i
        
        # 失敗判定：次に進めるドミノが見つからなかった場合
        # または、見つかったドミノが現在より大きくならない場合
        if next_idx == -1 or S[next_idx] <= S[last_idx]:
            count = -1
            break

        # 更新：見つかったドミノをチェーンに加え、次に進む
        count += 1
        last_idx = next_idx
        used[last_idx] = True
    
    print(count)

# --- main process---
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()