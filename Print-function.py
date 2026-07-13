# dsplay the result in python, we used print funcions

#syntax 1
print(val1)
     or
print(val1, val2, val3n)
>>> a = 12
>>> b = 32
>>> c = 43
>>> print(a, b, c)
12 32 43
------------------------------------------------------------------------------------------------------
#syntax 2
This syntax used for print the string message on console.
>>> print("hello python student")
hello python student
  
>>> print("hello", 'python', """student""")
hello python student
  
>>> print("hello"+'python'+"""student""")
hellopythonstudent

>>> print("hello"+ 'python'+ """student""")     <----- no , here
hellopythonstudent

>>> print("hello"+' python'+""" student""")
hello python student

---------------------------------------------------------------
#syntax 3
----------------------
print message cum value or value come message.

>>> print("value of a =", a)
value of a = 12

>>> print(a, "is the value of a")
12 is the value of a

>>> print("value of a =", a, "value of b =", b, "sum value of a and b =", c)
value of a = 12 value of b = 32 sum value of a and b = 43


>>> print(c, "is the sum of a & b")
30 is the sum of a & b

print("sum of", a, ",", b, "and", d, "is =", d)
---------------------------------------------------------------------------------------------------------------------
#syntax 4
--------------
#dispying the value in formate function.
>>> print("value of a=",(a))
value of a= 10
>>> print("vale of a={}".format(a))
vale of a=10


>>> print("val of a={}, val of b={}, is sum of a & b is {}" .format(a, b, c))
val of a=10, val of b=20, is sum of a & b is 30

>>> print("vale of a {}, value of b {}, value of c {}".format(30, 20 , 10))
vale of a 30, value of b 20, value of c 10

lst1=[1, 2, 3, 'qw', 'ew']
lst2=[6, 7, 3, "wq", "esd"]
>>> print("data in lst1={}, data in lst2={}".format(lst1, lst2))
data in lst1=[1, 2, 3, 'qw', 'ew'], data in lst2=[6, 7, 3, 'wq', 'esd']

----------------------------------------------------------------------------------------------------------------------
#syntax 5
-----------------------------
dispaying the vale throung specifuer %
>>> print("my sno number is {} and student name is {} and marks is {}".format(sno, name, marks))
my sno number is 10 and student name is rossom and marks is 7.9

>>> print("my sno number is %d and student name is %s and marks is %f" % (sno, name, marks))
my sno number is 10 and student name is rossom and marks is 7.900000

>>> print("here is the date for lst1{} and data for lst2{}".format(lst1,lst2))
here is the date for lst1[1, 2, 3, 'qw', 'ew'] and data for lst2[6, 7, 3, 'wq', 'esd']





----------------------------------------------------------------------------------------------------------------------
#syntax 6
displying the data in same line.

>>> for val in range(40,100):
...     print(val, end="-->")
...
40-->41-->42-->43-->44-->45-->46-->47-->48-->49-->50-->51-->52-->53-->54-->55-->56-->57-->58-->59-->60-->61-->62-->63-->64-->65-->66-->67-->68-->69-->70-->71-->72-->73-->74
>>>

>>> for val in range(40,100, 20):
...     print(val, end="-->")
...
>>> >60-->80-->






