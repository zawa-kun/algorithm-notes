# ABC381振り返り
[リンク](https://atcoder.jp/contests/abc381/tasks)
## A問題
### 自分の解答
以下を満たすとき"Yes"と出力するようにした.
1. Sの前半が全て1
2. Sの後半が全て2

必ず"No"になるのは,以下のパターン.
1. 文字列の長さが1
2. 文字列Sの長さが偶数

### 模範解答
上記のパターンに加えて,   
- **真ん中に"/"があるかの確認が必要になる**  

これをしないと「11122」等のパターンに対応出来なくなる。  

### 振り返り
- 把握出来ていないエッジパターンを減らすにはどうすればいいんだろうか.

↳考え得る対策
- 問題の入力条件をよく見て自分自身でも例だけで把握しきれていないパターンを試す.
- そもそも漏れが多そうな論理を組まない。

- エッジパターンは沼りやすいな。
## B問題
### 自分の解答
#### 考え方
以下の場合処理終了

- Ｔの長さが偶数でない
- T[2i-1] == T[2i]でない
- 各文字は必ず2文字
```Python
T = str(input())

# Tの長さが奇数の時処理終了.
if len(T) % 2 == 1 or len(T) == 0:
    print("No")
    exit()

# 1 <= i <= len(T)//2を満たすiについて
# T[2i-1] == T[2i]　を満たさない場合処理終了.
existed = []
for i in range(0,len(T)//2):
    # 以下の場合,処理終了.
    # ・T[2i-1] == T[2i]　を満たさない.
    # ・一つの文字が3回以上登場している.(いつの文字の出現数が2ではない.)
    if T[2*i] != T[2*i+1] or T[2*i] in existed:
        print("No")
        exit()
    existed.append(T[2*i])

print("Yes")
```
#### 自分のコードの問題点
・重複の判定を"in"を使ってしているから,計算量は悪そう.

### 模範解答
```Python
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
```
### 振り返り
**ord(c)**:cのユニコードを返す.
```Python
print(ord('a')) #97 (aのユニコード)
```
