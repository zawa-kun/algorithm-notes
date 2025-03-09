N = int(input())
TV = [list(map(int,input().split())) for _ in range(N)]
water = 0 # 水の総量
fin = TV[N-1][0]

for time in range(fin):
    # 水は0以下にはならない.
    if water != 0:
        water -= 1

    if TV[0][0] - 1 == time:
        water += TV[0][1]
        TV.pop(0) #効率悪いけど一旦この方法.

print(water)   
