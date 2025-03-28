# 📚 Algorithm Notes

このリポジトリは、アルゴリズムとデータ構造の学習記録をまとめたものです。基本的なアルゴリズムの説明、実装例、問題解決のノートを記録し、定期的に更新していきます。

## 📌 目標
✅ アルゴリズム・データ構造の理解を深める  
✅ コーディング面接や競技プログラミングの準備  
✅ 学習の進捗を可視化し、継続的に改善する  

---

## 📂 フォルダ構成

```
algorithm-notes/
│── README.md  # 学習の進捗や方針を書く
│── basics/    # 基礎的なアルゴリズム（ソート、探索など）
│── data_structures/  # データ構造（スタック、キュー、木、グラフなど）
│── problems/  # 解いた問題（AtCoder, LeetCode, Codeforces）
│── tips/  # アルゴリズムの考え方やよく使うテクニック
│── references.md  # 参考にした書籍やサイトをまとめる
```

---

## 🏗 進め方

### **1️⃣ 基礎的なアルゴリズムを整理する**
- `basics/` に、ソート・探索・動的計画法などのアルゴリズムを整理
- Markdown で説明を記述し、Python/C++ で実装例を追加

📌 **例：`basics/binary_search.md`（二分探索のノート）**
```md
# 🏹 二分探索（Binary Search）

## 概要
二分探索は、ソート済みの配列に対して高速に探索を行うアルゴリズム。  
計算量は O(log N)。

## 実装（Python）
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
```

---

### **2️⃣ 解いた問題を記録する**
- `problems/` に、AtCoder・LeetCode・Codeforces の解いた問題を追加
- **「問題の説明 + 解法 + 実装コード」** を Markdown にまとめる

📌 **例：`problems/atcoder_abc100_a.md`（AtCoderの問題ノート）**
```md
# 🏆 AtCoder ABC100 A問題「Happy Birthday!」

## 問題URL
https://atcoder.jp/contests/abc100/tasks/abc100_a

## 解法
- 2つの整数 A, B が 8以下なら "Yay!"、そうでなければ ":(" を出力。

## 実装（Python）
```python
a, b = map(int, input().split())
print("Yay!" if a <= 8 and b <= 8 else ":(")
```
```

---

## 🚀 GitHubへの更新方法

```bash
git add .
git commit -m "Add binary search notes"
git push origin main
```

---

## 📖 参考資料
- [アルゴリズム・データ構造 (AtCoder公式)](https://atcoder.jp/contests/dp)
- [競技プログラミングの鉄則](https://www.slideshare.net/iwiwi/ss-3578491)
- [LeetCode](https://leetcode.com/)

---

## 📢 今後の追加予定
✅ グラフアルゴリズム（BFS / DFS / ダイクストラ法）  
✅ 高度な動的計画法（bit DP, ナップザック問題）  
✅ 競技プログラミングのテクニック（累積和, Union-Find）  

---

📌 **学習の進捗を記録しながら、スキルを向上させていきます！ 💪🔥**