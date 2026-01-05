# Constraints
# 'a' <= s[i] <= 'z'

s = "azyxaaaxyyz"
m = ["d", "a", "x", "y"]

hash_list = [0]*26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val-97
    hash_list[index] += 1
for ch in m:
    asci_val = ord(ch)
    index = asci_val-97
    print(hash_list[index])
