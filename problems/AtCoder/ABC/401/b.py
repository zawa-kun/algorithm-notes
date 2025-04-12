N = int(input())

login = False
err_cnt = 0
for i in range(N):
    S = str(input())
    if S == 'login':
        login = True
        continue
    elif S == 'logout':
        login = False
        continue

    if login == False and S == 'private':
        err_cnt += 1

print(err_cnt)

        
