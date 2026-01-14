def merge_arrays(nums1, nums2):
    i, j = 0, 0
    n = len(nums1)
    m = len(nums2)
    result = []
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j]) 
            j += 1
    while i < n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    while j < m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1                
    print(result)
    return result
    
arr1 = [1, 1, 2, 3, 5, 7, 7, 9]
arr2 = [1, 2, 2, 4, 6, 8, 9, 10]
merge_arrays(arr1, arr2)