A, B, C = map(int, input().split())

if B <= C: # ex) 3-7
    if A <= B or C <= A:
        print("Yes")
    else:
        print("No")
else: # ex) 7-3
    if C <= A and A <= B:
        print("Yes")
    else:
        print("No")