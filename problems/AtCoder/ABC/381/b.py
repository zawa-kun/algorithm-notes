T = str(input())

# Tの長さが奇数の時処理終了.
if len(T) % 2 == 1 or len(T) == 0:
    print("No")
    exit()

# 1 <= i <= len(T)//2を満たすiについて
# T[2i-1] == T[2i]　を満たさない場合処理終了.
existed = []
for i in range(0,len(T)//2):
    #重複の判定を"in"を使ってしているから,計算量は悪そう.
    if T[2*i] != T[2*i+1] or T[2*i] in existed:
        print("No")
        exit()
    existed.append(T[2*i])

print("Yes")