def subset_sum(nums, target):
    N = len(nums)
    for i in range(1 << N):
        current_sum = 0
        current_subset = []
        for j in range(N):
            if (i >> j) & 1:
                current_sum += nums[j]
                current_subset.append(nums[j])
            
        if current_sum == target:
            print(f"見つかりました: 合計 {target} をなす部分集合：{current_subset}")
            return True
    
    print(f"合計 {target} をなす部分集合は見つかりませんでした。")
    return False

nums1 = [1, 2, 4, 7]
target1 = 13
subset_sum(nums1, target1)

nums2 = [1, 5, 10]
target2 = 3
subset_sum(nums2, target2)