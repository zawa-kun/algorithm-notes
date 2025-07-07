T = int(input())

for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    """
    問題点１「ドミノの情報を失ってしまっている」
    本来、ドミノ1からスタートし、ドミノNで終わる」という制約がある。
    sortを実行してしまうと、どの大きさがどのドミノに対応するか分からなくなる。
    """
    S.sort() # 昇順ソート
    

    """
    問題点２「連鎖の作り方が逆」
    小さいものから大きいものにしていく必要がある。
    """
    dominos = []
    dominos.append(S.pop()) # 最初の要素を置く

    # ここから貪欲法でSj <= 2Siを満たせば置く。という事を繰り繰り返す。
    while S:
        if S[-1] <= 2 * dominos[-1]:
            dominos.append(S.pop())
        else:
            S.pop()
    
    if len(dominos) >= 2:
        print(len(dominos))
    else:
        print(-1)

    