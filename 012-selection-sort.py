def selection_sort(arr):
    n = len(arr)
    for i in range(0,n):
        # min_index = i
        max_index = i
        for j in range(i+1,n):
            # if(arr[j]<arr[min_index]):
            #     min_index = j
            if(arr[j]>arr[max_index]):
                max_index = j
        # arr[min_index],arr[i]=arr[i],arr[min_index]
        arr[max_index],arr[i]=arr[i],arr[max_index]
        print(arr)
         

nums=[64, 25, 12, 22, 11]
selection_sort(nums)