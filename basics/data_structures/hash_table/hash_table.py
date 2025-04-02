import hashlib
from typing import Any

class HashTable(object):
    def __init__(self, size=10) -> None: # indexの数を10に設定
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    # indexを求める
    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size
    
    def add(self, key, value) -> None:
        index = self.hash(key) # get the index
        key_exists = False

        for data in self.table[index]:
            # 既にKeyが存在しているとき,valueのみ上書き
            if data[0] == key:
                key_exists = True
                data[1] = value
                break
        
        if not key_exists:
            self.table[index].append([key, value])
    
    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')
            print()
    
    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
    
    """Pythonと同じ呼び出し方をする為の定義"""
    def __setitem__(self, key, value) -> None:
        self.add(key, value)
    
    def __getitem__(self, key) -> Any:
        return self.get(key)





if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('car', 'Tesla')
    hash_table.add('car', 'Toyota')
    hash_table.add('pc', 'Mac')
    hash_table.add('sns', 'Youtuber')
    hash_table.print()
    print(hash_table.get('pc'))