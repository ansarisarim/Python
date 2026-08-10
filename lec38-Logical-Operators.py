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
