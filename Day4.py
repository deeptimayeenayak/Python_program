#Q1.
'''dic={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
l=list(input().split())
p=o=e=0
for i in l:
    if i=='P':
        p+=1
    elif i=='O':
        o+=1
    elif i=='E':
        e+=1
if (p>o and p>e):
    print(dic['P'])
elif (o>p and o>e):
    print(dic['O'])
elif (e>p and e>o):
    print(dic['E'])
#Q2
s1=input()
s2=input()
s=""
for i in s1:
    if i in s2 and i!=' ':
        s+=i
print(s)

#OOPS using Python
#Q1
class Example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        self.num=num

    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

#Q2
class Customer:
    def __init__(self):
        self.cust_id = 100

cl=Customer()
print(cl.cust_id)//Error=

#Q3
class Customer:
    def __init__(self,id):
        self.id = 100

cl=Customer(200)
print(cl.id)

#Q4
class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"

my_fav.title="Learning Python"

print("My favorite is",my_fav.title)
print("Yours's is",my_fav.title)

#Q5
class Shoe:
    def __init__(self,price, material):
        self.price = price
        self.material = material

    def __str__(self):
        return "Shoe with price: " + str(self.price) + "and material:" + self.material

s1=Shoe(1000, "Canvas")
print(s1)

#Q6
class Mobile:
    def display(self):
        print("Displaying Details")

    def purchase(self):
        self.display()
        print("Calculating Price")

Mobile().purchase()


#Q7
class Mobile:
    def __init__(self, brand, price):
        self.price = price
        self.brand = brand
        self.total_price = None
        
    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price- self.price*(discount / 100)
        print("Total price of", self.brand, "mobile is",self.total_price)
mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000)
mob1.purchase()
mob2.purchase()

#Q8
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def show_balance(self):
            print("The balance is ",self.__wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()
#print(c1.__wallet_balance)-->Throws error

#Q9
class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_wallet_balance(self, amount):
        if amount < 1000 and amount>  0:
            self.__wallet_balance = amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())'''
'''
#q10
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None

    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top

    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(True, False)
print(rate)
'''

#Q11
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,front_table,back_table)













