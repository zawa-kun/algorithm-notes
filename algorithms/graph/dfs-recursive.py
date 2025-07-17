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
            