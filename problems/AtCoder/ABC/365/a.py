Y = int(input())
flag_366 = False

if Y % 4 == 0:
    if Y % 100 != 0:
        flag_366 = True

if Y % 400 == 0:
    flag_366 = True
    
if flag_366:
    print(366)
else:
    print(365)