def array_sorted(arr):
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True
    
nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 3, 4, 1, 2]
print(array_sorted(nums1))  # Output: True
print(array_sorted(nums2))  # Output: False