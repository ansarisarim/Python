Definition:


# logical operators is to combaine two or more relational expressions. 

1) "and" Operator
--------------------------------

>>> True and True...........True
>>> False and True..........False
>>> False and False.........False
>>> True and False..........False

>>> 10>2 and 30>100.........False
>>> 10>2 and 30>40...........False
>>> 10>2 and 30>20...........True  full length evaluation
>>> 10>2 and 30>40............False 
>>> 10>2 and 30>20............True
>>> 10>2 and 30>20 and 30>2.............True   
>>> 10>2 and 30>20 and 30>200...............False
>>> 30>300 and 10>2 and 30>20...............False    short circuit evaluation 

Definition:  
"In AND operator, if the first condition is False, Python stops checking remaining conditions and 
directly returns False. This is called Short Circuit Evaluation. If all conditions are True, Python checks every
condition, called Full Length Evaluation."
--------------------------------------------------------------------------------------------------------------------------------------------

2) "or" Operator
--------------------------------
>>> 10>20 or 20>30 or 30>40.............False
>>> 20>10 or 30>20 or 40>30.............True
>>> 10>20 or 30>40 or 50>30.............True
>>> 50>10 or 40>30 or 50>100............True
--------------------------------------------------------------------------------------------------------------------------------------------

3) "not" Operator
--------------------------------

>>> not False
True
>>> not True
False
>>> not 0
True
>>> not 1
False

>>> not str(10-10)
False    <-----"0"
>>> str(0)
'0'

>>> not str(10-10)
False
>>> str(0)
'0'




# Strings
not "hello"     # False (non-empty → True → not → False)
not ""          # True  (empty → False → not → True)
not " "         # False (space bhi non-empty!)

# Numbers
not 0           # True  (0 → False → not → True)
not 1           # False (1 → True  → not → False)
not 5           # False (any number → True → not → False)

# List
not []          # True  (empty list → False → not → True)
not [1,2,3]     # False (non-empty → True → not → False)

# None
not None        # True  (None → False → not → True)



OR  = Pehli TRUE mili  → STOP! → TRUE
AND = Pehli FALSE mili → STOP! → FALSE


--------------------------------------------------------------------------------------------------
special point ....."and"    (and → Pehla False mile toh wahi return, warna last value return)
>>> 10 and 500
500
>>> 0 and 500
0

>>> 234 and 10-10 and 43
0

>>> True and True and False
False

>>> False and True and True
False

>>> "java" and "python" and "data science"
'data science'


--------------------------------------------------------------------------------------------------
special point ....."or"  (or → Pehla True mile toh wahi return, warna last value return)

>>> 100 or 100
100
>>> 100 or 2
100
>>> 0 or 2
2
>>> True or False or False
True
>>> False or False or True
True
