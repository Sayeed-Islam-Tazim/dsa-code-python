def func(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if(s[left] != s[right]):
            print("The given string is not a palindrome")
            return False
        left += 1
        right -= 1
    print("The given string is a palindrome")
    return True

word = "madam"
func(word)