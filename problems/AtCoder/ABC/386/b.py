s = [int(i) for i in input()]
count = 0 # ボタンを押す回数.
zero_flag = False # zeroの個数を管理するフラグ.

while len(s) != 0:
    count += 1

    # "00"か"0"の判断.
    if zero_flag:
        if s[-1] ==  0:
            zero_flag = False
        else:
            zero_flag = False
            count -= 1
    # if s[-1] == 0 and zero_flag == False:
    #     zero_flag = True

    print("要素:",s[-1],"count:", count, "zero_flag", zero_flag)
    s.pop() # 配列の最後を取り出す.

print(count)
    