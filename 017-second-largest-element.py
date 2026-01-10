def sec_large(arr):
    largest = second_largest = float('-inf')
    n = len(arr)
    for i in range(0, n):
        if(arr[i] > largest):
            second_largest, largest = largest, arr[i]
        elif(arr[i] > second_largest and arr[i] != largest):
            second_largest = arr[i]
    return second_largest

nums = [12, 35, 1, 10, 34, 1 ,-5, -6, -19]
print(sec_large(nums))