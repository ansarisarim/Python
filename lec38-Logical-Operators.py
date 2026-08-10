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



OR  = Pehli TRUE mili  → STOP! → TRUE
AND = Pehli FALSE mili → STOP! → FALSE
