A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

AB_2 = (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2
AC_2 = (A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2
BC_2 = (C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2

if AB_2 + AC_2 == BC_2:
    print("Yes")
elif AB_2 + BC_2 == AC_2:
    print("Yes")
elif BC_2 + AC_2 == AB_2:
    print("Yes")
else:
    print("No")