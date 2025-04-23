class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

# 要素の挿入
def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)
    
    # 左＜真ん中＜右　の関係を再帰的呼び出し構築
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

# 昇順で表示
def inorder(node: Node) -> None:
    # いろんな木の見方
    # Inorder Left, Root, Right
    # Preorder Roor, Left, Right
    # Postorder Left, Right, Root
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def search(node: Node, value: int) -> bool:
    if node is None:
        return False
    
    if node.value == value:
        return True
    
    elif value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)

def min_value(node: Node) -> Node:
    current = node
    while current.left is not None:
        current = current.left
    return current

def remove(node: Node, value: int) -> None:
    if node is None:
        return node
    
    if value < node.value: # 小さければ左側を見ていく
        node.left = remove(node.left, value)
    elif value > node.value: # 大きければ右側を見ていく
        node.right = remove(node.right, value)
    else: # valueと要素が一致したとき
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
    
        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value) # 右側にあるものを移動させていく。

    return node


if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    inorder(root)
    print('###################')
    root = remove(root, 6)
    inorder(root)