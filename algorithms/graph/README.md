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

