def move_zeroes_to_right(nums):
    n = len(nums)
    temp = []
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])
    nz = len(temp)
    for i in range(0, nz):
        nums[i] = temp[i]
    for i in range(nz, n):
        nums[i] = 0
    
arr =[0,1,0,3,12]
move_zeroes_to_right(arr)
print(arr)  # Output: [1,3,12,0,0]