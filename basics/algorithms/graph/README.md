# グラフ関連のアルゴリズム
---
## グラフの表現方法
- 隣接リスト (Adjacency List)
- 隣接行列 (Adjacency Matrix)

--- 
## 探索方法
- DFS（深さ優先探索）
- BFS（幅優先探索）
- Union-Find（素集合データ構造）

---
## DFS（深さ優先探索）
### イメージ
1. 一本通路を決める
2. 壁にぶつかるまで進む
3. ぶつかったら、来た道を一つ戻り、まだ試していない別の通路があるときはそっちに進む

2, 3 を繰り返し、すべて探索する。

### 実装
主に２つの方法がある
- 再帰
- スタック

再帰実装の例
```Python
def dfs(graph, start_node):
    visited = set() # 訪問済みを記録するセット

    def _dfs_recursive(node):
        visited.add(node)
        print(f"訪問: {node}") # 可視化用
        
        # 現在のノードに隣接するノードを探索
        for neighbor in graph[start_node]:
            if neighbor not in visited:
                _dfs_recursive(neighbor) # 未訪問であるとき再帰的にDFSを呼び出す。
    
    _dfs_recursive(start_node)

graph_example = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2]
}

print("---DFSの実行")
dfs(graph_example, 0)       
```
```shell
---DFSの実行
訪問: 0
訪問: 1
訪問: 2
訪問: 3
```

### 実用例
- 連結成分の探索：グラフがいくつに分割されているか。　それぞれのノードがどのノードで構成されているかを見ることができる
- 経路探索：あるノードから別のノードへ到達可能か調べること出来る。
- サイクル検出：グラフの中に閉路があるかどうかを調べることができる。

#### AtCoderではどんなふうに出てくるか
- 迷路探索
- 連結成分の数え上げ

---

## BFS
スタートノードから近いノード順に、層をなすように探索を進めていく。

### イメージ

1. スタートノードの決定
2. 距離１のノードをすべて探索
3. 距離２のノードをすべて探索

### 実装
- キュー(queue)で実装

```Python
from collections import deque

def bfs(graph, start_node):
    visited = set()             # 訪問済みノード
    queue = deque([start_node]) # キューに開始ノードをセット
    visited.add(start_node)     # 開始ノードを訪問済みに
    distance = 0

    print(f"---BFSの実行(開始：{start_node}---")
    while queue:
        current_node = queue.popleft() # キューからノードを取り出す
        print(f"訪問: {current_node}, 距離：{distance} ")

        if len(queue) == 0:
            distance += 1
        # 現在のノードに隣接するノードを表示
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor) # 未訪問であれば訪問済みにする
                queue.append(neighbor) # キューに追加
        


graph_example = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0, 3],
    3: [0, 1, 2, 4],
    4: [3]
}

if __name__ == "__main__":
    bfs(graph_example, 0)
```

### BFSの活用例
- 最短経路問題(重み無しグラフ) : スタートから他ノードまでの最短経路を求めることができる
- 最短手数の問題
- ある状態から別の状態へ遷移するのに、最短で何手かかるかを求める問題に応用
- グラフの層を調べることができる：スタートノードから距離が等しいノードの集合を取得できる

#### AtCoderでの使い道
「最短経路」や「最短手数の移動といった問題でBFSが非常に頻繁に使われる」
- 最小何歩でゴールにたどり着けるかはBFSの典型的な応用例

---

## Union-Find（素集合データ構造）
※グラフアルゴリズムというよりはデータ構造！

要素をいくつかの互いに素な集合に分割し、以下の２つの操作を効率的に行うためのデータ構造

- **Union(結合)** : ２つの要素が含まれる集合を結合
- **Find(探索)** : ある要素がどの集合に属しているかを探索

### Union-Findのイメージ
あるクラスの担任だとして、生徒たちをグループ分けする。

この時
- Find：「Ａさんはどのグループ？」と聞かれたら、すぐにその代表者を答える
- Union : 「ＢさんとＣさんを同じグループにして」と言われたとき、別々のグループであれば、その２つのグループを１つに結合。


### 実装
- `parent`配列：各要素の親を記録
- `rank`(または`size`)配列：木の深さを調整を効率化を図る

上記の二つを使い、実装

```Python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))    # parent[i] : 要素iの親(初期状態は自分自身が親[0, 1, 2....n-1])
        self.size = [1] * n             # size[i] : iが根であるときの集合のサイズ(初期状態サイズ１（全て独立しているため)
    
    # 要素x の根を検索
    def find(self, x):
        # x自身が根であるとき, x自身を返す
        if self.parent[x] == x: 
            return x

        # 経路圧縮：根に直接つなぎ直す
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # 要素xとyが含まれる集合を結合する
    # Union by Size (またはRank)により高速化
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # 異なる集合に属していれば結合
        if root_x != root_y:
            # サイズの小さい方を大きい方につなげることで木の深さを抑える
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x # root_x を大きい方にそろえる

            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            return True
        return False
    
    def is_same_set(self, x, y):
        return self.find(x) == self.find(y)
    
    # 要素xが属する集合のサイズを返す
    def get_size(self, x):
        return self.size[self.find(x)]
```


