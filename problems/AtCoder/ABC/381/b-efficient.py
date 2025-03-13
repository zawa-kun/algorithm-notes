s = input() # 変数名を小文字sにする事で英子文字を受け取る事を示せる.
flag = True

if len(s)%2==1:
    flag = False

# s[s*i] == s[2*i+1]
if flag:
    for i in range(len(s)//2):
        if s[2*i] != s[2*i+1]:
            flag = False
        
# 各文字の出現数を計算していく
cnt = [0 for i in range(26)] # 26:sに使われる候補となる文字の種類数(英子文字の種類)
if flag:
    #各文字が何個含まれているか確認
    for i in range(len(s)):
        cnt[ord(s[i])-ord('a')]+=1
    # ０個か２個か確認.
    for i in range(26):
        if cnt[i] != 0 and cnt[i] != 2:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
