def right_rotate(nums,k):
    n = len(nums)
    rotations = k % n
    # 1st Solution
    # for _ in range(0, rotations):
    #     nums[:] = [nums[n-1]] + nums[0:n-1]
    # 2nd Solution
    nums[:] = nums[n-rotations:n] + nums[0:n-rotations]
    # 3rd Solution
    # reverse_nums(nums, n-rotations, n-1)
    # reverse_nums(nums, 0, n-rotations-1)
    # reverse_nums(nums, 0, n-1)
    # 4th Solution
    # for _ in range(0, rotations):
    #     last_element = nums.pop()
    #     nums.insert(0, last_element)

# def reverse_nums(nums, left, right):
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
        
arr= [ 1,2,3,4,5,6,7 ]
k = 3
right_rotate(arr,k)
print(arr)  # Output: [5,6,7,1,2,3,4]