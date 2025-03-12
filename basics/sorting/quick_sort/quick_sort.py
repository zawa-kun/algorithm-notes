from typing import List

def partition(numbers: List[int], low: int, high: int) -> int:
    pass

def quick_sort(numbers : List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high) # Pivotの配列インデックスを受け取る.
            _quick_sort(numbers, low, partition_index-1)    # Pivotより左側.
            _quick_sort(numbers, partition_index+1, high)   # Pivot寄り左側.
            
    # partition(numbers, low, high)


if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5,7]
    print(quick_sort(nums))