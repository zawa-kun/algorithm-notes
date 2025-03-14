from typing import List

def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    # 最初の要素から順に整列されていくため、
    # 見る範囲を狭めていく.
    for i in range(len_numbers):
        # 最も小さい数字を仮置き.
        min_idx = i
        for j in range(i+1, len(numbers)):
            #一番小さい値を探す
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        #一番小さい数字を今見ている部分の最も小さい場所におく.
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]    
    return numbers

if __name__ == '__main__':
    nums = [1, 5, 2, 8, 7, 8]
    print(selection_sort(nums))