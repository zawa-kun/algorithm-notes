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
