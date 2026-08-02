# Single line assighnment aperators.
>>> a=12
>>> b=8
>>> c=a+b
>>> print(a,b,c)
12 8 20
------------------------------------------------------------------------------------------------------------

# Multiline assighnment aperators.
for assighning the RHS value to LHS
>>> a,b=10,3
>>> c,d,e,f=a+b,a/b,a-b,a*b
>>> print(c)
13
>>> print(d)
3.3333333333333335
>>> print(e)
7
>>> print(f)
30
>>>


-------------------------------------------------------------------------------------
a,b=(input("inter the first number:" ), input("inter the second nu,ber:"))
print("org value of a is {}" .format(a))
print("org value of b is {}" .format(b))

print("*"*50)
a,b=b,a
print("swap value of a:{}".format(a))
print("swap value of b:{}".format(b))
