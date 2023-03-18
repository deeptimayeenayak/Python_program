#List Comprehension
#for loop version
'''result=[]
for i in range(11):
    result.append(i)
print(result)
#list comprehension version
print([i for i in range(11)])
#for loop version-->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
l=[]
for i in range(8):
    for j in range(8):
        if i==0 or j==0 or i==7 or j==7:
            print('----',end=" ")
        else:
            print((j,i),end=" ")
    print()
#List Comprehension
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([ele**2 if ele%2!=0 else ele**3
       for row in mat for ele in row])
print([[ele**2 if ele%2!=0 else ele**3 for ele in row]
       for row in mat])

#Q1
mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)

print([(i,mylist.index(i))for i in list_b])
#Q2
sentences=["a new world record was set","in the holy city of ayodhya",
           "on the eye of diwali on tuesday","with over three lakh diya or earthen lamps",
           "lit up simunltaneously on the banks of the sarayu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']
results=[]
for sentence in sentences:
    sentence_t=[]
    for word in sentence.split(' '):
        if word not in stopwords:
            sentence_t.append(word)
    results.append(sentence_t)
print(results)

#q3
a=list(map(int,input().split(",")))
number1=sum(array[S:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in l:
    number2+=str(i)
print(int(number2)+number1)''' 

#q4
num=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1:]+ss[:-1]
    else:
        return ss[-2:]+ss[:-2]













