# Constraints
# 1 <= n[i] <= 10
# n can have 10^8 elememtns
# m can have 10^8 elememtns

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
hash_list = [0]*11
for nums in n:
    hash_list[nums] += 1
for i in m:
    if (i > 10 or i < 1):
        print(0)
    else:
        print(hash_list[i])
