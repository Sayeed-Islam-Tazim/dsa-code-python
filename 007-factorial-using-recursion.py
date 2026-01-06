def func(n):
    if(n==0):
        return 1
    # return n * func(n-1)
    fact = n * func(n-1)  
    print(n,'! =',fact)
    return fact
    
func(10)