prices = list(map(int,input().split()))
C = str(input())

# color -> index の対応付け
color_index = {"Red": 0, "Green": 1, "Blue": 2}
del prices[color_index[C]]

print(min(prices))