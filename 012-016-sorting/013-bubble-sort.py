def bubble_sort(arr):
    # n = len(arr)
    # # Traverse through all array elements
    # for i in range(n):
    #     # Last i elements are already sorted
    #     for j in range(0, n-i-1):
    #         # Traverse the array from 0 to n-i-1
    #         # Swap if the element found is greater than the next element
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #     print(arr)
    # return arr
    n = len(arr)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0, i+1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                is_swap=True
        print(arr)
        if(is_swap==False):
            break
        
         
nums1=[64, 25, 12, 22, 11]
nums2=[11, 12, 22, 25, 64]
bubble_sort(nums2)
