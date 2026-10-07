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
another approache
---------------------
a=float(input("inter the value of a: "))
b=float(input("inter the value of b: "))
c=float(input("inter the value of c: "))
if (b<=a>c):
    print("a={}, b={}, c={} in this a={} is bigger value".format(a, b, c, a))
if (a<b>c) :
    print("a={}, b={}, c={} in this b={} is the bigger value". format(a, b, c, b))
if (a==b==c):
    print("a={}, b={}, c={} all are same value".format(a, b, c) )
print("program completed")

--------------------------------------------------------------------------------------------------------------------------------------------------
Q2. Write a python program which will accept  digit and display its name ?

a=int(input("Enter the Number: "))
if a==1:
    print("{} is one".format(a))
if a==2:
    print("{} is two".format(a))
if a==3:
    print("{}, is the three".format(a))
if a==4:
    print("{}, is the Four".format(a))
if a==5:
    print("{}, is the Five".format(a))
if a==6:
    print("{}, is the Six".format(a))
if a==7:
    print("{}, is the Seven".format(a))
if a==8:
    print("{}, is the Eight".format(a))
if a==9:
    print("{}, is the Nine".format(a))
if a<0:
    print("{} is the -ve digit".format(a))
if a not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and a>0 :
     print("inter correct value")

--------------------------------------------------------------------------------------------------------------------------------------------------
# little modification in above code.
a=int(input("Enter the Number: "))
if a==1:
    print("{} is one".format(a))
if a==2:
    print("{} is two".format(a))
if a==3:
    print("{}, is the three".format(a))
if a==4:
    print("{}, is the Four".format(a))
if a==5:
    print("{}, is the Five".format(a))
if a==6:
    print("{}, is the Six".format(a))
if a==7:
    print("{}, is the Seven".format(a))
if a==8:
    print("{}, is the Eight".format(a))
if a==9:
    print("{}, is the Nine".format(a))
if a not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and a<0 :
    print("inter correct value")



simple if statement.........its check all the if statment its take lots of proccessing time thats why furthe will use ifelse statment to aovoid unneccesary proccesing will see in next slide.
