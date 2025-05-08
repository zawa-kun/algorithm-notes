H = int(input())

H_plant = 0
day = 0

while True:
    H_plant += 2 ** day
    if H_plant > H:
        print(day+1)
        exit()
    day += 1