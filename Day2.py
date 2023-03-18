'''#list-->Ordered--default index
#
list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=[10,20.2,30+3j,True,"Python"]
print(list3,type(list3))
list4=list([100,200,300,400])
print(list4,type(list4))
list5=[101,201,301,401]
print(list5,type(list5))
list5.append(501)
print(list5,type(list5))
#list5.insert(0->index,51->value)
print(list5,type(list5))
list5.remove(301)
print(list5,type(list5))
list5.pop()#last element will pop
print(list5,type(list5))
list5.pop(0)
print(list5,type(list5))
del list5[1]
print(list5,type(list5))
#Q1
def func(s):
    alpha=0
    digit=0
    for i in s:
        if i.isalpha():
            alpha=alpha+1
        if i.isdigit():
            digit=digit+1
    return[alpha,digit]
s=input()
print(func(s))
#Q2
def func(arr,n):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==n:
                count+=1
    return count
arr=eval(input("Enter your list:"))
target=int(input())
print(func(arr,target))
#Q3
def func(s):
    if(len(s)<2):
        return -1
    elif(len(s)==2):
        return s*2
    else:
        return s[:2]+s[-2:]
s=input()
print(func(s))
#Q4
def func(s):
    if(len(s)<3):
        return s
    elif(s[-3:]=="ing"):
        return s+"ly"
    else:
        return s+"ing"
s=input()
print(func(s))
#Q5
def func(n):
    doub=str(n*2)
    num=str(n)
    c=0
    for i in num:
        if i in doub:
            c+=1
        else:
            return False
            break
    if c==len(num): return True
n=int(input())
print(func(n))'''


#Q7
def func(d,words):
    word2=[]
    for i in words.split():
        if i in d:
            word2.append(d[i])
    return word2
d={"merry":"god", "christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
words="merry christmas and happy new year"
print(func(d,words))

            






