def two_sum(nums, target):
    n=len(nums)    
    # Best Approach
    hash_map = {}
    for i in range(n):
        compliment = target - nums[i]
        if compliment in hash_map:
            return [hash_map[compliment], i]
        hash_map[nums[i]] = i
    
    # 1st Approach
    # for i in range(n):
    #     compliment = target - nums[i]
    #     if compliment in nums and nums.index(compliment) != i:
    #         return [i, nums.index(compliment)]
    
    # 2nd Approach
    # for i in range(0, n-1):
    #     for j in range(i+1, n):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

arr1 = [2,7,11,3,4,15,6,10]
arr2 = [3,2,4]
targetVal = 6 #17
print(two_sum(arr2, targetVal))