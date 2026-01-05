# Constraints
# 1 <= nums[i] <= 10
# nums can have 10^8 elememtns
# m can have 10^8 elememtns

nums = [5, 6, 7, 4, 2, 1, 4, 6, 7, 4]
m = [10, -3, 2, 5, 7, 8, 67, 4, 111]
hash_map = {}
for i in range(0, len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i], 0)+1
print("hash_map ", hash_map)
print("m ", m)
for i in m:
    if (i > 10 or i < 1):
        print(0)
    else:
        print(hash_map.get(i, 0))
