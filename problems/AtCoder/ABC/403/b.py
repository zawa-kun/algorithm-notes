T = str(input())
U = str(input())

T_length = len(T)
U_length = len(U)

for ti in range(T_length):
    if T[ti] == "?" or T[ti] == U[0]:
        if T_length - ti < U_length:
            print("No")
            exit()

        flag = True
        for ui in range(U_length):
            if T[ti+ui] != U[ui] and T[ti+ui] != "?":
                flag = False # T[ti+ui]がU[ui]でも?でも無いとき
        if flag:
            print("Yes")
            exit()
