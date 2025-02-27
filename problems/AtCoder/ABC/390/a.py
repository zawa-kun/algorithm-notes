A = [int(i) for i in input().split()]

if A[0] == 2 and A[1] == 1 and A[2:5] == [3, 4, 5]: # 2,1,3,4,5
    print("Yes")
elif A[1] == 3 and A[2] == 2 and A[0] == 1 and A[3:5] == [4, 5]: # 1,3,2,4,5
    print("Yes")
elif A[2] == 4 and A[3] == 3 and A[0:2] == [1, 2] and A[4] == 5: # 1,2,3,4,5
    print("Yes")
elif A[3] == 5 and A[4] == 4 and A[0:3] == [1, 2, 3]: # 1,2,3,4,5
    print("Yes")
else:
    print("No")

