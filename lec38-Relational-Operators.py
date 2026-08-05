Operator	Meaning	True Example	False Example	
#ERROR!	Equal to	5 == 5  →  True	5 == 3  →  False	
!=	Not equal to	5 != 3  →  True	5 != 5  →  False	
>	Greater than	10 > 5  →  True	5 > 10  →  False	
<	Less than	3 < 8  →  True	8 < 3  →  False	
>=	Greater than or equal to	5 >= 5  →  True	4 >= 5  →  False	
<=	Less than or equal to	4 <= 7  →  True	8 <= 7  →  False	


  
>>> "wow">="woW"
True
>>> ord("w")
119
>>> ord("W")
87
-------------------

Q. Write a python program which demonstare the consecpt of relational operators?

a=int(input("inter your first value "))
b=int(input("inter your second value "))

print("-"*50)

print("\t \t {} >= {} =  {}".format(a,b, a >= b ))
print("\t \t {} >= {} =  {}".format(a,b , a <= b))
print("\t \t {} == {} =  {}".format(a,b,a==b))
print("\t\t {} != {}  =  {}".format(a,b,a!=b))
print("\t\t {} > {}   =  {}".format(a,b,a>b))
print("\t\t {} < {}   =  {}".format(a,b,a<b))

