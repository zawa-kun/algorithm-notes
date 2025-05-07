prices = list(map(int,input().split()))
C = str(input())

if C == "Red":
    prices.pop(0)
elif C == "Green":
    prices.pop(1)
elif C == "Blue":
    prices.pop()


print(min(prices))
    
