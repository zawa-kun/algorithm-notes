def rev(num: int) -> int:
    num_str = str(num)
    rev_num_str = num_str[::-1]
    return int(rev_num_str)
    
    

a_list = [0]*10

a_list[0], a_list[1] = map(int, input().split())

cnt = 1 # 10まで繰り返すから

while cnt != 9:
    cnt += 1
    x = a_list[cnt-2] + a_list[cnt-1]
    a_list[cnt] = rev(x)

print(a_list[9])