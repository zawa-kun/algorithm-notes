A = input().split()

color = set(A)

if len(color) == 1:
    print(2)
    exit()
elif len(color) == 2:
    # 2種類の時は、同じ色が2つあるかどうかを確認
    if A.count(A[0]) == 2: # 例）3, 3, 4, 4,
        print(2)
    else: # 例）3, 4, 4, 4
        print(1)
elif len(color) == 3:
    print(1)
    exit()
else:
    print(0)


