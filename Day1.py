#Q1
#Decision making statements
#read a number
#multiple 3
#multiple 
#multipla of 3 AND 5
"""n = int(input())
if(n % 3 ==0 and n %5 == 0):
    print("Multiple of 3 and 5")
elif(n %5 == 0):
    print("Multiple of 5")
elif(n%3==0):
    print("Multiple of 3")
else:
    print("Invalid")"""
#Q2
'''for i in range(1,101):
   print(i)
for i in range(1,101,2):
    print(i,end=" ")
for i in range(2,101,2):
    print(i,end=" ")

for i in range(100,0,-1):
    print(i,end=" ")
print()

for i in range(100,0,-2):
    print(i,end=" ")
print()'''
#Q3
'''for i in range(1,101):
    if(i==50):
        continue
    print(i,end=" ")
for i in range(1,101):
    if(i==50):
        pass
    print(i,end=" ")
#Function
def function1():
    print("its a function1")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
function2(10,20)
def function3(num1,num2):
    num3=num2+num1
    return num3
print("value reurned",function3(100,200))
def function4(num1,num2):
    num3=float(num1)+num2
    return num3
print("value reurned",function4('10',20.2))
def function5(num1,num2):
    num3=num2+num1
    return num3
print("value reurned",function3(10,20.2))'''

#categories of function
#based on arguments
#1:positional arguments
def functional1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
functional1(10,20,30,40)
functional1(100,200,300,400)
#2:Keyword Arguments
def functional1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
functional1(num4=10,num3=20,num2=30,num1=40)
functional1(num4=10,num1=10,num2=30,num3=40)#right to left
#3:Default argumenyts
def function3(name,rollno,branch,clgname="Giet"):
    print(name,rollno,branch,clgname)
function3("deepti",237,"CSE")
function3("gulsan",235,"CSE")
function3("souri",240,"CSE")
function3("gouri",242,"CSE")
#4:variable no of arguments
def function4(*var):
    for i in var:
        print(i,end='')

function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)
print()

def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))










        
