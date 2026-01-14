def missingNumber(nums):
        n = len(nums)
    # Best Approach
        return (n*(n+1)//2) - sum(nums)

    # 1st Approach
        # total = 0
        # for i in nums:
        #     total = total + i
        # return (n*(n+1)//2) - total

    # 2nd Approach
        # nums.sort()
        # for i in range(0, n+1):
        #     if i < len(nums):
        #         if i != nums[i]:
        #             return i
        #     else:
        #         return i

    # 3rd Approach
        # for i in range(0, n+1):
        #     if i not in nums:
        #         return i
         
    # 4th Approach
        # freq = {}
        # for i in range(0, n+1):    
        #     freq[i] = 0
        # for num in nums:
        #     freq[num] = 1
        # for k,v in freq.items():
        #     if v == 0:
        #         return k
    
arr1 = [3,0,1]
arr2 = [0,1]
print(missingNumber(arr1))
print(missingNumber(arr2))