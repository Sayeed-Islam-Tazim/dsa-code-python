def remove_duplicate(arr):
    n = len(arr)
    if n == 1:
        return 1
    i = 0
    j = i + 1
    while j < n:
        if arr[j] != arr[i]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    return i + 1 , arr[0:i+1]

nums = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 10]
print(remove_duplicate(nums))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]