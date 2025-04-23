class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(object):
    
    def __init__ (self) -> None:
        self.root = None

    # 要素の挿入
    def insert(self, value: int) -> None:

        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)
            
            # 左＜真ん中＜右　の関係を再帰的呼び出し構築
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        
        _insert(self.root, value)
    
    # 昇順で表示
    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)


    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False
            
            if node.value == value:
                return True
            
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)
    
    

    def min_value(node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def remove(self, value: int) -> None:
        def _remove(node: Node, value: int) -> None:
            if node is None:
                return 
            
            if value < node.value: # 小さければ左側を見ていく
                node.left = _remove(node.left, value)
            elif value > node.value: # 大きければ右側を見ていく
                node.right = _remove(node.right, value)
            else: # valueと要素が一致したとき
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
            
                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value) # 右側にあるものを移動させていく。

            return node
        _remove(self.root, value)
    

        


if __name__ == '__main__':
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(2)
    binary_tree.insert(1)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(10)
    binary_tree.inorder()