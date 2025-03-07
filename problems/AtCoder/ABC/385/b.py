# #は通行停止
# .は通行可能 and 家無し
# @は通行可能 and 家有り

"""
H:縦 W:横
(X,Y):最初にいる場所
"""
H, W, X, Y = map(int, input().split())
G = [list(input()) for _ in range(H)]
T = list(str(c) for c in input())

# 1 <= X,Y のため,配列のインデックスに合わせる.
X = X - 1
Y = Y - 1 

visited_home = [] #訪問済み家のリスト.

for count in range(len(T)): # 指示の数分動く.
    #通行可能のとき
    if T[count] == "U" and G[X - 1][Y] != "#":
        if G[X - 1][Y] == "@" and [X - 1, Y] not in visited_home: # 家有∧まだ訪ねていない
            visited_home.append([X - 1, Y])
            X, Y = X - 1, Y # 移動
            continue
        else: #家無し
            X, Y = X - 1, Y # 移動
    elif T[count] == "D" and G[X + 1][Y] != "#":
        if G[X + 1][Y] == "@" and [X + 1, Y] not in visited_home: # 家有∧まだ訪ねていない
            visited_home.append([X + 1, Y])
            X, Y = X + 1, Y # 移動
            continue
        else: #家無し
            X, Y = X + 1, Y # 移動
    elif T[count] == "L" and G[X][Y - 1] != "#":
        if G[X][Y - 1] == "@" and [X, Y - 1] not in visited_home: # 家有∧まだ訪ねていない
            visited_home.append([X, Y - 1])
            X, Y = X , Y - 1 # 移動
            continue
        else: #家無し
            X, Y = X, Y - 1 # 移動
    elif T[count] == "R" and G[X][Y + 1] != "#":
        if G[X][Y + 1] == "@" and [X, Y + 1] not in visited_home: # 家有∧まだ訪ねていない
            visited_home.append([X, Y + 1])
            X, Y = X, Y + 1 # 移動
            continue
        else: #家無し
            X, Y = X, Y + 1 # 移動

#debug: output grid
# for y in range(W):
#     for x in range(H):
#         print(G[x][y],end="")
#     print()

print(X + 1, Y + 1, len(visited_home))