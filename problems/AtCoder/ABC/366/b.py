from typing import List

# 渡された単語の中で最長の長さを取得
def get_max_vocab_length(vocabs: List[str]) -> int:
    max_len = -1
    for vocab in vocabs:
        if max_len < len(vocab):
            max_len = len(vocab)
    
    return max_len + 1


def solution(vocabs: List[str]) -> None:
    max_len = get_max_vocab_length(vocabs)
    G = [['*']*len(vocabs) for _ in range(max_len)]
    y = len(vocabs) - 1
    for i in range(len(vocabs)): # tanngo
        x = 0
        for j in range(len(vocabs[i])): # moji
            if len(vocabs[i]) > j:
                G[x][y] = vocabs[i][j]
            x += 1
        y -= 1

    print(''.join(G[i]))
    
    

if __name__ == '__main__':
    N = int(input())
    vocabs = [str(input()) for _ in range(N)]
    solution(vocabs)