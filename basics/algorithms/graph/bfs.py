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
    bfs(graph_example, 1)
