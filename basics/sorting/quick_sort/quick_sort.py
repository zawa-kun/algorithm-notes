from typing import List

# pivotよりも大きい物がどんどん右に小さい物は左に移っていく.
def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1 # 入れ替える場所のインデックス.
    pivot = numbers[high]

    # pivot寄りも大きい数字がどんどん右に寄っていく.
    # 最終的なj:pivotが入るであろうインデックス.
    for j in range(low, high):
        if numbers[j] <= pivot: 
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    # pivotを適切な位置に挿入.
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    # pivotのインデックスを返す.
    return i+1 


def quick_sort(numbers : List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high) # Pivotの配列インデックスを受け取る.
            _quick_sort(numbers, low, partition_index-1)    # Pivotより左側.
            _quick_sort(numbers, partition_index+1, high)   # Pivot寄り左側.
    
    _quick_sort(numbers, 0, len(numbers)-1) # 配列を全て渡す.
    return numbers


if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5,7]
    print(quick_sort(nums))