A, B, C, D = map(int, input().split())

if A == C and B > D:
    print("Yes")
elif A > C:
    print("Yes")
else:
    print("No")