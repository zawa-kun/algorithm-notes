N, X, Y, Z = map(int, input().split())


if X <= Z and Z <= Y and X < Y:
    print("Yes")
elif Y <= Z and Z <= X and Y < X:
    print("Yes")
else:
    print("No")