def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_arr = merge_sort(left_half)
    right_arr = merge_sort(right_half)
    return merge_array(left_arr, right_arr)


def merge_array(left, right):
    i, j = 0, 0
    result = []
    n, m = len(left), len(right)
    while i < n and j < m:
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if (i < n):
        while i < n:
            result.append(left[i])
            i += 1
    if (j < m):
        while j < m:
            result.append(right[j])
            j += 1
    return result


nums = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(nums))  # Output: [3, 9, 10, 27, 38, 43, 82]
