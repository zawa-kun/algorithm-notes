world, stage = map(int, input().split("-"))
if stage < 8:
    print(str(world) + "-" + str(stage+1))
elif world < 8 and stage == 8:
    print(str(world+1)+"-"+str(1))
else:
    print("1-1")
