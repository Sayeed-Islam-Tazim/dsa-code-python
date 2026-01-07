def insertion_sort(arr):
    for i in range(1,len(arr)):
        # if(arr[i])<arr[i-1]:
        #     key=arr[i]
        #     j=i-1
        #     while(key<arr[j]):
        #         arr[j+1]=arr[j]
        #         j-=1
        #         if(j<0):
        #             break
        #     arr[j+1]=key
        # print(arr)
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)

nums=[3,5,6,4,8,9,10,7,2,1]
insertion_sort(nums)      
        