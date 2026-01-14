def rearrange_element_by_sign(nums):

    # 1st Approach
    for i in range(0, len(nums)):
        j = i + 1
        if nums[i] >= 0 and j < len(nums):
            while nums[j] >= 0:
                j += 1
            nums[j], nums[i+1] = nums[i+1], nums[j]
        else:
            continue
        if nums[i] < 0 and j < len(nums):
            while nums[j] < 0:
                j += 1
            nums[j], nums[i+1] = nums[i+1], nums[j]
        else:
            continue 
    return nums
    
    
    # 2nd Approach
    # pos = []
    # neg = []
    # for num in nums:
    #     if num >= 0:
    #         pos.append(num)
    #     else:
    #         neg.append(num)
    # for i in range(0, len(pos)):
    #     nums[2*i] = pos[i]
    #     nums[2*i + 1] = neg[i]
    # return nums
    
    # 3rd Approach (Optimal)
    # n = len(nums)
    # result = [0] * n
    # pos_index, neg_index = 0, 1
    # for num in nums:
    #     if num >= 0:
    #         result[pos_index] = num
    #         pos_index += 2
    #     else:
    #         result[neg_index] = num
    #         neg_index += 2
    # return result

arr1 = [4, -2, 5, 6, -7, -1]
arr2 = [-1, 1]
arr3 = [1, -1]
print(rearrange_element_by_sign(arr3))  # Output: [4, -2, 5, -7, 6, -1]