from typing import List

def calculate_tiredness(N: int, AS: List):
    # 左手・右手が存在するかをチェック
    has_L = any(hand == 'L' for _, hand in AS)
    has_R = any(hand == 'R' for _, hand in AS)

    # 初期化
    current_L = None
    current_R = None

    # 最初の左手・右手の位置を設定
    for value, hand in AS:
        if hand == 'L' and has_L and current_L is None:
            current_L = int(value)
        elif hand == 'R' and has_R and current_R is None:
            current_R = int(value)
        if (not has_L or current_L is not None) and (not has_R or current_R is not None):
            break

    tiredness = 0
    for i in range(1, N):
        value = int(AS[i][0])
        hand = AS[i][1]
        if hand == "L":
            if current_L is not None:
                tiredness += abs(value - current_L)
            current_L = value
        elif hand == "R":
            if current_R is not None:
                tiredness += abs(value - current_R)
            current_R = value

    return tiredness

if __name__ == '__main__':
    N = int(input())
    AS = [input().split() for _ in range(N)]
    print(calculate_tiredness(N, AS))
