def solve():
    N = int(input())
    S = str(input())

    S = "0" + S # 状態0を安全として追加

    ok = [False]*(2**N) # ok[i]: 状態iに到達可能か否か
    ok[0] = True # 初期状態（何も混ざっていないときは到達可能）

    # すべての状態を昇順に走査
    for i in range(1 << N):
        if not ok[i]:
            continue

        # まだ混ぜていない薬品jを追加する事を試みる
        # 薬品は１～Nまでなので、ｊは０～Ｎ－１に対応
        for j in range(N):
            if (i >> j) & 1:
                continue # 既に含まれている薬品は追加できない
            
            # 現在の状態iに薬品j+1を追加
            # コンピュータは内部的には数字を２進数で取り扱っているため、変換する必要なくAND演算できる
            next_state = i | (1 << j)

            if S[next_state] == '0': 
                ok[next_state] = True
        
    if ok[(2**N) - 1]:
        print("Yes")
    else:
        print("No")

# テストケースの数Tを読み込む
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()