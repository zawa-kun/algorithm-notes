# この2パターンの時、Yes
# xが3枚and yが1枚
# xが2枚 and yが2枚

cards = [int(i) for i in input().split()]

if len(set(cards)) == 2:
    print("Yes")
else:
    print("No")
