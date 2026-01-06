n=[0,1,2,3,4,5,6,7,8,9,10]
def arrayReverse(arr,left,right):
    # while(left<right):
    #     arr[left],arr[right]=arr[right],arr[left]
    #     left+=1
    #     right-=1
    # print(arr)
    if(left>=right):
        print(arr)
        return
    arr[left],arr[right]=arr[right],arr[left]
    arrayReverse(arr,left+1,right-1)

arrayReverse(n,2,8)