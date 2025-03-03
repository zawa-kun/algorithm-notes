# バブルソート(Bubble Sort)　O(n²)
## 概要
**隣合う要素を比較**し、**大きい方（小さい方から）徐々に並び替えていく**ソートアルゴリズム

## 手順
1. 配列の先頭から隣り合う要素を比較し、順番が逆の場合交換.
2. 1回の走査が終わると、最大（最小）の要素が端に移動する.
3. 残り(len(arr) - 1 -i番目まで)の要素について同じ処理を繰り返す.

## 計算量
| 最良計算量 | 平均計算量 | 最悪計算量 | 空間計算量 |
|------------|------------|------------|------------|
| O(n) (すでにソート済み) | O(n²) | O(n²) | O(1) (追加のメモリ不要) |

### 補足説明
- **最悪計算量 O(n²)** : すべての要素が逆順のとき、完全な2重ループが必要.
- **最良計算量 O(n)** : すでにソート済みなら、1回のループで終了(改良版のみ).
- **空間計算量 O(1)** : 配列を直接変更するため、追加メモリをほとんど使用しない.

## 使い道
- 簡単に実装したいとき.
- 小規模なデータに対するソート.