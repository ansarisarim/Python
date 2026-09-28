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



