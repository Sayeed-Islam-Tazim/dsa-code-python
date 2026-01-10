def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[j], nums[low] = nums[low], nums[j]
    return j


def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index-1)
        quick_sort(nums, pivot_index+1, high)


nums = [38, 27, 43, 3, 9, 82, 10]
quick_sort(nums, 0, len(nums)-1)
print(nums)  # Output: [3, 9, 10, 27, 38, 43, 82]
