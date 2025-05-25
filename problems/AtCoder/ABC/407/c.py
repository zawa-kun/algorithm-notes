S = input()
S_list = [int(s) for s in S]

A_cnt = 0
B_cnt = 0
while len(S_list) > 0:
    num = S_list[-1]
    if B_cnt % 10 > num:
        num = 10 + num - B_cnt % 10
    else:
        num -= B_cnt % 10
    
    B_cnt += num
    A_cnt += 1
    S_list.pop()
    
print(A_cnt + B_cnt)