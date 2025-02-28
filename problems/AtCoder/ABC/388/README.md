# ABC388振り返り
[リンク](https://atcoder.jp/contests/abc388/tasks)
## A問題

### 解法メモ
- Sの１文字目を出力し、改行せずにUPC出力.

### 模範解答

### 振り返り
- 特になし.

## B問題

### 解法メモ
- N匹目まで長さを1~D伸ばしたときの重量を計算し,最大の最大の値を出力する.

### 模範解答
- 同じ.
### 振り返り
- 変数の受取方として,
```入力
4 3
3 3
5 1
```
受取方
```Python
T, L = [0]*N, [0]*N
for i in range(N):
    T[i], L[i] = map(int, input().split())

#内包表記で書くとこんな感じ.
T, L = map(list, zip(*(map(int, input().split()) for _ in range(N))))
```