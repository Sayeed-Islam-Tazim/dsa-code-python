for n in range(100, 2001):
    num = n
    total = 0
    nod = len(str(n))
    while num > 0:
        ld = num % 10
        total = total+(ld**nod)
        num = num//10
    if (n == total):
        print(n)

# modified
# --------
# inp1=int(input("Give Lower Bound: "))
# inp2=int(input("Give Higher Bound: "))

# print("Armstrong numbers are below: ")
# for n in range(inp1,(inp2+1)):
#     num=n
#     total=0
#     nod=len(str(n))
#     while num>0:
#         ld=num%10
#         total=total+(ld**nod)
#         num=num//10
#     if(n==total):
#         print(n)
