def func(s,left,right):
    if(left>=right):
        print("The given string is palindrome")
        return True
    if(s[left]!=s[right]):
        print("The given string is not palindrome")
        return False
    func(s,left+1,right-1)
    
s = "madame"
func(s,0,len(s)-1)