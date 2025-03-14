from typing import List 
def merge_sort(numbers: List[int]) -> List[int]:
    """分割セクション"""
    # 分割した要素が1以下になったら,mergeが始まる.
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)        # 分割し、要素が1になったときに返ってくる.
    merge_sort(right)       # 上に同じ

    """マージ"""
    i = 0   # i:leftのインデックス管理
    j = 0   # j:rightのインデックス管理
    k = 0   # k:挿入時のインデックス管理
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1 #挿入位置をずらす.
    
    
    # 上のwhile文ではright,rightどちらかの全ての要素を挿入し終わるとループが停止するため,
    # 残った要素を並び替えなくては行けない.
    # 左側が残った場合
    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1
    # 右側が残った場合
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1
    
    return numbers

if __name__ == "__main__":
    numbers = [5, 4, 1, 8, 7, 3, 2, 9]
    print(merge_sort(numbers))