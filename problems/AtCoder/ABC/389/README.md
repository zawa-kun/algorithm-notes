# ABC389振り返り
[リンク](https://atcoder.jp/contests/abc389/tasks)
## A問題

### 解法メモ
- int(S[0])*int(S[2])を出力する.１文字目×３文字目
### 模範解答
```Python
s = input() # 入力を受け取る
a = int(s[0]) # 1文字目の値
b = int(s[2]) # 3文字目の値
print(a * b)
```

### 振り返り
- 特になし.

## B問題

### 解法メモ
- x!~2!順番に計算していき,x == n!となるようなnを探す.
↑ x = 2432902008176640000の時に途方もない時間がかかってしまったため無し.
- 2!から順番に計算.
↑ x は最大で,3×10^18であるため,nの最大もそこまで大きくない.

### 模範解答
- 1から順番に階乗を計算していって,x = n!となるようなnを出力.

### 振り返り
- 階乗は再帰関数で書いていた.再帰関数も書けるようにならないとな.