Example-1
a = str(input("do you have the ticket yes/no : ")).lower()

if(a=="yes"):
    print("get entry in the premises")
    print("Find out your chair and sit there")
    print("enjoy the show!!!")

print("go back to home please")

--------------------------------------------------------------------------------------------------------------------------------
Example-2

Q. write a python program which will accept accept two numerical values and find bigest amoung them and check for equality 
by using simple if statment.

a=float(input("Enter the first value: "))
b=float(input("Enter the second value: "))
if(a>b):
    print("{}, {} in this {}, is grater value".format (a,b,a))
if (a<b):
    print("{}, {} in this {}, is less value".format(a,b,a))
if (a==b):
    print("{},{}, both value are equal".format(a,b))
print("process finished")


--------------------------------------------------------------------------------------------------------------------------------
Example-3
a=str(input("you have the adhar card: " )).lower()
if(a=="yes"):
    print("submit the xerox copy")
    print("write down the adhar number")
if(a=="no"):
    print("adhar is mandatory please come with the adhar card")
if a not in ["yes", "no"]:
    print("please enter yes or no")
print("\t thanx for your support")
