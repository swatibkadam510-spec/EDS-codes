import math
n=int(input())
if n<10:
    print(n*n)
elif (n>=10 and n<=99):
    result = math.sqrt(n)
    print(f"{math.sqrt(n):.2f}")
elif (n>=100 and n<=999):
    result = n**(1/3)
    print(f"{n**(1/3):.2f}")
else:
    print("invalid")