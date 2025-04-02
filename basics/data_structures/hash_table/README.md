# ハッシュテーブル（Hash Table）

## 概要

ハッシュテーブルは、キーと値のペアを格納するためのデータ構造で、高速な検索、挿入、削除操作を提供します。ハッシュ関数を使用してキーを配列のインデックスに変換することで、O(1)の平均時間複雑度でのアクセスを実現します。

## 仕組み

1. **ハッシュ関数**: キーをテーブル内の位置（インデックス）に変換する関数
2. **衝突解決**: 異なるキーが同じインデックスにマッピングされた場合の解決方法
3. **テーブルサイズ**: データ格納のための配列の大きさ

## 実装方法

### ハッシュ関数

良いハッシュ関数の条件:
- 計算が高速である
- キーを均等に分散させる
- 同じキーは常に同じハッシュ値を返す

一般的なハッシュ関数の例:
```python
def hash(key):
    return key % table_size  # 数値キーの場合
```

文字列の場合:
```python
def hash(key):
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % table_size
    return hash_value
```

### 衝突解決方式

#### 1. チェイニング（開放アドレス法）

同じインデックスに複数の要素を格納するために、各インデックスにリンクリストを用意します。

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self, key):
        return hash(key) % self.size
    
    def add(self, key, value):
        index = self.hash(key)
        
        for data in self.table[index]:
            if data[0] == key:  # 既存のキーを更新
                data[1] = value
                break
        else:
            self.table[index].append([key, value])  # 新しいキーを追加
    
    def get(self, key):
        index = self.hash(key)
        
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
        
        return None  # キーが見つからない場合
```

#### 2. 線形探索法（閉鎖アドレス法）

衝突が発生したとき、次の空き位置を順番に探索します。

```python
def add(self, key, value):
    index = self.hash(key)
    
    while self.table[index] is not None and self.table[index][0] != key:
        index = (index + 1) % self.size  # 次のインデックスを試す
    
    self.table[index] = [key, value]
```

## ハッシュテーブルの性能

### 時間複雑度
- 検索: 平均 O(1)、最悪 O(n)
- 挿入: 平均 O(1)、最悪 O(n)
- 削除: 平均 O(1)、最悪 O(n)

### 空間複雑度
- O(n) - nはキーと値のペアの数

## 使用例

```python
# ハッシュテーブルの初期化
hash_table = HashTable(10)

# データの追加
hash_table.add("name", "太郎")
hash_table.add("age", 30)
hash_table.add("city", "東京")

# データの取得
name = hash_table.get("name")  # "太郎" が返される
```

## 実際の応用

- 辞書やマップの実装
- データベースのインデックス
- キャッシュの実装
- 重複要素の検出
- 頻度カウント

## 注意点

- 適切なハッシュ関数の選択
- ロードファクター（要素数/テーブルサイズ）の管理
- リハッシュのタイミング（テーブルサイズの動的調整）

## まとめ

ハッシュテーブルは、大量のデータから特定の要素を高速に検索する必要がある場合に非常に効果的なデータ構造です。適切に実装すれば、ほぼ定数時間での操作が可能になり、多くのアプリケーションのパフォーマンスを大幅に向上させることができます。