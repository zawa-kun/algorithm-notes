# C
左右一列N個のマス

最初すべて白

クエリ

- 左からAi番目のマスを色反転させる

- その後黒マスが連続になっている区間の個数を求める


反転させたマスの左右に注目

- 両方白なら＋１
- 左右＋２の範囲が黒の時はー１
- 左＋２または右＋２の範囲はー２ 違う？
- 左右＋１の範囲が黒の時は＋１

白＝０
黒＝１


く　し　く　し　く　し　く　く　し
　　⇓
　　く
　　＋１


はじの処理どうすればいいんだー

この考え方も間違ってはいないが、ロジックが複雑になってしまう。

## 正答
i と i+1 が「違う」かどうかの境界を管理

隣接マスの「違い」を管理し、境界数から区間数を導出

（処理時間O(Q)（1クエリあたりO(1)で安定）


### コアとなる考え方
**区間数＝境界数／2**という発想

境界の変化は１クエリで高々２か所(A-1, A)しか影響しない

その為、常にO(1)という時間で処理できる

