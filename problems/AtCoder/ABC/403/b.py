T = str(input()) # ?moji
U = str(input()) # hirabun

T_len = len(T)
U_len = len(U)
j = 0

for i in range(len(U)):
    while len(T) - i - 1 > 0:
        print('T[j]:', T[j], "U[i]", U[i])
        if U[i] == T[j] or T[j] == '?':
            break
        j += 1
    print('--------next----------')

