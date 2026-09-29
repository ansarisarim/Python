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

-------------------------------------------------------------------------------------------
# write apython program whic will decide either word have wovel or not
word = input("Enter a word: ")

result = "Vowel alphabet" if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word else "Not a Vowel Alphabet"

print("{} word has the {}".format(word, result))

-------------------------------------------------------------------------------------------
# write a apython program which wil accept the word and decide whether it is palandrom or not
a = input("inter the value ")
result= "palandrom value" if a==a[::-1] else "not palandrom value"
print("{}, is {} " .format(a,result))


