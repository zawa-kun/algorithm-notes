from typing import List

# 渡された単語の中で最長の長さを取得
def get_max_vocab_length(vocabs: List[str]) -> int:
    max_len = -1
    for vocab in vocabs:
        if max_len < len(vocab):
            max_len = len(vocabs)
    
    return max_len + 1
        
def solution(N: int, vocabs: List[str]) -> None:
    max_len = get_max_vocab_length(vocabs)
    G = [list(str())*len(vocabs) for _ in range(max_len)]
    # y = len(vocabs)
    for i in range(len(vocabs)): # tanngo
        x = 0
        for j in range(max_len): # moji
            if len(vocabs[i]) > j:
                G[x].append(vocabs[i][j])
            elif max_len - i  - 1 == j :
                G[x].append("*")
            x += 1
    
    print(G)
    

    # 詰め込んでいって、最後にアスタリスク追加。

    

if __name__ == '__main__':
    N = int(input())
    vocabs = [str(input()) for _ in range(N)]
    solution(N, vocabs)