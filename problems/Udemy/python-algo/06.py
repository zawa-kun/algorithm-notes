from typing import List, Tuple, Optional

def get_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
            

def get_pair_ans(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in nums:
        cache.add(num)
        val = target - num
        # targetからnumを引いたものがcache内にあるときその２数が答え
        if val in cache:
            return val, num


def get_pair_half_sum(nums: List[int]) -> Optional[Tuple[int, int]]:
    sum_nums = sum(nums)
    # if sum_nums % 2 != 0:
    #     return
    """ ⇓⇓ divmod を使うと下のように書ける ⇓⇓"""
    half_sum, reminder = divmod(sum_nums, 2)
    if reminder != 0:
        return

    half_sum = int(sum_nums / 2)

    cache = set()
    for num in nums:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num






if __name__ == '__main__':
    nums = [11, 2, 5, 9, 10, 3]
    target = 12
    print(get_pair(nums, target))
    print(get_pair(nums, target))

    print(get_pair_half_sum(nums))

    
