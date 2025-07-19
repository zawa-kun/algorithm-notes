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
    

if __name__ == "__main__":
    """Union-Findの動作例"""
    uf = UnionFind(5) # 1, 2, 3, 4, 5の要素で初期化

    print(f"0と1は同じ集合か？ : {uf.is_same_set(0, 1)}")
    
    print("0, 1 結合")
    uf.union(0, 1)
    print(f"0と1は同じ集合？ : {uf.is_same_set(0, 1)}")
    print(f"0の集合サイズは？：{uf.get_size(0)}")
