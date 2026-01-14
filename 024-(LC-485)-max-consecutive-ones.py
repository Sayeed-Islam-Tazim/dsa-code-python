def consecutive_ones(nums):
    count = 0
    max_count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)
        
arr1 = [0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0]
arr2 = [0,0,0,0,0,0,0]
arr3 = [1,1,0,1,1,1]
print(consecutive_ones(arr1))

