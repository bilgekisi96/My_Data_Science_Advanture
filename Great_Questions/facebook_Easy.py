"""
This problem was asked by Facebook.
Given three 32-bit integers x, y, and b,
return x if b is 1 and y if b is 0,
using only mathematical or bit operations.
You can assume b can only be 1 or 0.

"""



def calc():
    x,y,b=int(input("enter 32 bir number: ")),int(input("enter 32 bir number: ")),int(input("Enter only 0 or 1: "))
    return y + b*(x-y)
print(calc())
















