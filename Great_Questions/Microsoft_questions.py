
"""
This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28

"""
def perfnum(a):
    if sum([int(i)for i in  str(a)])==10:return print("perfect number")
    elif (10-sum([int(i)for i in  str(a)]))>0:return print(str(a)+str(10-sum([int(i)for i in  str(a)])) )
    else:return print("not perfect")
perfnum(100)

