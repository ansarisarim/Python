Q. Write a python program which will accept 3 numarical value and find the biggest amoung them and check for equality.

a=float(input("inter the value of a: "))
b=float(input("inter the value of b: "))
c=float(input("inter the value of c: "))
if (a>b) and (a>c):
    print("{}, {}, {} in this {} is bigger value".format(a, b, c, a))
if (b>a) and (b>c):
    print("{}, {}, {} in this {} is the bigger value". format(a, b, c, b))
if (a==b) and (a==c) and (b==c):
    print("{}, {}, {} is the same value".format(a, b, c) )
print("program completed")

--------------------------------------------------------------------------------------------------------------------------------------------------
