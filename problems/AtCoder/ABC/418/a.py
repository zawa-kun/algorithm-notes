N = int(input())
S = list(input())

if N < 3:
    print("No")
    exit()

if S[-3] == "t" and S[-2] == "e" and S[-1] == "a":
    print("Yes")
else:
    print("No")