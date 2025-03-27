A = list(map(int, input().split()))

cnt = [0] *13
for i in range(len(A)):
    # 各数字の出現数を数える。
    cnt[A[i]-1]+=1


# 2と3が含まれているか確認
if 2 in cnt:
    if 3 in cnt or 4 in cnt or 5 in cnt:
        print("Yes")
        exit()
elif 3 in cnt and 4 in cnt:
    print("Yes")
    exit()
elif cnt.count(3) == 2:
    print("Yes")
    exit()
print("No")
