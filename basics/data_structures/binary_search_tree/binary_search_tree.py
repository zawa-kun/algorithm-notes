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



if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    # inorder(root)
    print(search(root, 10))
    print(search(root, 11))
    # print(root.value)               # 3
    # print(root.right.value)         # 6
    # print(root.right.left.value)    # 5
    