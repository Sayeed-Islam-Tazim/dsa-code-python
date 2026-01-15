def longest_consecutive_sequence(nums):
    # 1st Approach
    # nums.sort()
    # count = 0
    # last_smallest = nums[0]
    # longest_streak = 0
    # for num in nums:       
    #     if num-1 == last_smallest:
    #         count += 1
    #     elif num != last_smallest:
    #         count = 1
    #     last_smallest = num
    #     longest_streak = max(longest_streak, count)
    # return longest_streak
    
    
    # 2nd Approach -> Using Set
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        if num-1 not in num_set:
            x = num
            count = 1
            while x+1 in num_set:
                count += 1
                x += 1
            longest_streak = max(longest_streak, count)
    return longest_streak
            
arr1 = [1,1,1,2,3,5,98,99,100,101] # Output: 4
arr2 = [0,3,7,2,5,8,4,6,0,1] # Output: 9
arr3 = [10,5,12,3,55,30,4,11,2] # Output: 4
print(longest_consecutive_sequence(arr2))
