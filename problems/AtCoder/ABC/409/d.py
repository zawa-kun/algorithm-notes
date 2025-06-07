T = int(input())
cases = [[0,""] for _ in range(T)]
for i in range(T):
    cases[i][0] = int(input())
    cases[i][1] = input()

for case in cases:
    if case[0] == 1:
        print(case[1])
        continue # 1の時は次のケースへ
    
    str_len = case[0]
    str = case[1]
    ord_str = [0] * str_len
    for i in range(str_len):
        ord_str[i] = ord(str[i])
    print(str, ":",ord_str)
    min = sorted(ord_str)[0]
    sec_min = sorted(ord_str)[1]
    if str_len.index(min) == 0:
            
    print(min)