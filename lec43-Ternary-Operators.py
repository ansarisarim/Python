a=float(input("enter first value "))
b=float(input("inter second value "))
# print bigger value
bigvalue=a if a>b else b
print("bigvalue from {}, {} ={}".format(a,b,bigvalue))


-------------------------------------------------------------------------------------------

a=float(input("enter first value "))
b=float(input("inter second value "))
#biggervalue os same value
result= a if a>b else b if b>a else "both values are equal"
print("big({},{})={}".format(a,b,result))




-------------------------------------------------------------------------------------------

n = float(input("Enter the number --> "))
result = "Value is Positive" if n > 0 else "Value is Negative" if n == 0 else "Value is Zero"
print(result)




-------------------------------------------------------------------------------------------

Q. write a python program which will accept the numerical iteger value or float vale and decide whether it is even or od?
% baaki nikaalta hai (remainder)
10 ÷ 2 = 5  (baaki 0)
15 ÷ 2 = 7  (baaki 1)

a= float( input ("enter the first value --> "))
resulte = "even" if a%2==0 else "odd"
print("{}, is {}".format(a,resulte))


-------------------------------------------------------------------------------------------
# write a code to know value is od or even and ovoide the negative value
a=float(input(" enter the value please "))
result= "its a negative value" if a < 0 else "even" if a %2 == 0 else "odd"
print(result)




