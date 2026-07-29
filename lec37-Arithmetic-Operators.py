Arithmetic Operators — Notes

+  → Addition → a+b
-  → Subtraction → a-b
*  → Multiplication → a*b
/  → Division → a/b → hamesha float return karta hai (decimal)
// → Floor Division → a//b → decimal ke baad ka part hata deta hai (round down)
** → Exponent (power) → a**b → matlab a ka b power (a^b)
-----------------------------------------------------------------------------------------------------------


>>> a=10
>>> b=3
>>> print(a+b)
13

>>> print(a-b)
7

>>> print(a*b)
30

>>> print(a/b)
3.3333333333333335

>>> print(a//b)
3

>>> print(a**b)
1000

--------------------------------------------------------------------------
>>> print(10/3)
3.3333333333333335

>>> print(10//3)
3

>>> print(10.0/3.0)
3.3333333333333335

>>> print(10.0//3.0)                         <------------------ if value is in float then float is preferable
3.0

>>> print(10.0//3)                           <------------------ if value is in float then float is preferable
3.0
--------------------------------------------------------------------------------------

b=int(input("enter value of b "))
print("*"*50)
print("result of arithmetic operators")
print("\t sum {},{} ={}".format(a,b,a+b))
print("\t sub {},{} ={}".format(a,b, a-b))
print("\t mul {},{} ={}".format(a,b, a*b))
print("\t div {},{},={}".format(a, b, a/b))
print("\t floordiv {},{}={}".format(a, b, a//b))
print("\t expo {},{}={}".format(a,b, a**b))

------------------------------------------------------------------------------------------------

