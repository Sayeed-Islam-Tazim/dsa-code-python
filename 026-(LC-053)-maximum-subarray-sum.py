def max_subarray_sum(nums):
    maxi = float("-inf")
     
    # Brute Force Approach: O(n^2) time complexity
    # for i in range(0, len(nums)):
    #     total = 0
    #     for j in range(i, len(nums)):
    #         total = total + nums[j]
    #         maxi = max(maxi, total)
    # return maxi

    # Optimal Approach: Kadane's Algorithm -> O(n) time complexity
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        maxi = max(maxi, total)
        print("Before i:", i, "Total:", total, "Maxi:", maxi)
        if total < 0:
            total = 0
        print("After  i:", i, "Total:", total, "Maxi:", maxi)
    return maxi
        
    
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr2 = [-22, -11, -3, -4, -51, -12, -11, -5, -14]
arr3 = [22, 11, 3, 4, 51, 12, 11, 5, 14]
print(max_subarray_sum(arr1))  

# Output of arr1: 6
# Output of arr2: -3
# Output of arr3: 133