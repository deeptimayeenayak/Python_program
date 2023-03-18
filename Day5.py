#1
'''def check_type(type):
    vehicle_type=['TwoWheeler', 'FourWheeler']
    if type not in vehicle_type:
            return 0
    return 1
class Vehicle:
    def __init__(self):
        self.__vehicle_cost=None
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__premium_amount=None
        
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_type(self,vehicle_type):
        if check_type(vehicle_type):
            self.__vehicle_type=vehicle_type
        else:
            return "invalid Vehicle DETAILS"
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount
        
    def calculate_premium(self):
        if self.__vehicle_type=="TwoWheeler":
            self.__premium_amount=self.__vehicle_cost*2/100
        elif self.__vehicle_type=="FourWheeler":
            self.__premium_amount=self.__vehicle_cost*6/100
        else:
            print("Invalid Vehicle Type")
            
    def display_vehicle_details(self):
        print(self.__vehicle_type, self.__vehicle_cost, int(self.__premium_amount))
    
v1 = Vehicle()
#v1.set_vehicle_id=10
v1.set_vehicle_type(input())
v1.set_vehicle_cost(int(input()))
v1.calculate_premium()
v1.display_vehicle_details()


#Q2
courses = {1001:25575 , 1002:15500}
class Student:
    def __init__(self):
        self.__student_age=None
        self.__student_id=None
        self.__student_mark=None
        self.__student_fees=None
        self.__course_id=None

    def set_student_age(self,student_age):
        self.__student_age=student_age
    def get_student_age(self):
        return self.__student_age

    def set_student_id(self,student_id):
        self.__student_id=student_id
    def get_student_id(self):
        return self.__student_id

    def set_student_mark(self,student_mark):
        self.__student_mark=student_mark
    def get_student_mark(self):
        return self.__student_mark

    def validate_age(self):
        if self.__student_age>=20:
            return True
        else:
            return False

    def validate_marks(self):
        if self.__student_mark>=65 and self.__student_mark<=100:
            return True
        else:
            return False

    def check_qualifi(self):
        if self.validate_age() and self.validate_marks():
            return "Qualified Student"
        else:
            return "Disqualified Student"

    def get_student_fees(self):
        return self.__student_fees

    def get_courseid(self):
        return self.__course_id

    def check_courses(self, courseid):
        if courseid in courses:
            self.__course_id = courseid
            if self.__student_mark >= 85:
                self.__student_fees = courses[self.__course_id]*0.75 #because above 85 marks, 75% discount applied
            else:
                self.__student_fees = courses[self.__course_id] #because below 85 marks, no discount applied
            return True
        return False

s = Student()
s.set_student_id(int(input("Enter the student ID: ")))
s.set_student_age(int(input("Enter the student age: ")))
s.set_student_mark(int(input("Enter the student mark: ")))
#s.validate_age()
#s.validate_marks()
print(s.check_qualifi())

s.check_courses(int(input("Enter Course ID (1001 or 1002): ")))
print(s.get_student_fees())

'''
#3
'''

PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min
Customer can either collect the order in person or opt for a door delivery.
Write a python program based on the class diagram given below.

Customer class:
validate_quantity(): A customer can order 1 to 5 pizzas
If quantity is valid, return true. Else return false
Pizzaservice class:
Initialize static variable counter to 100
Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
True – additional topping is required, False – additional topping is not required
validate_pizza_type(): Customers can order "small" or "medium" type pizzas
If pizza type is valid, return true. Else return false
calculate_pizza_cost(): Calculate pizza cost
Validate pizza type and quantity
If valid,
Identify pizza cost based on details mentioned in the table
Set attribute, pizza_cost with the calculated pizza cost
Auto-generate service_id starting from 101 prefixed by first letter of pizza type. Example – S101, s102, m103, S104, M105 etc
If invalid, set pizza_cost to -1

PizzaType Cost/Pizza(in Rs) Additional topping cost/Pizza (in Rs), if applicable
Small 150 35
Medium 200 50

Doordelivery class:
validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
Validate distance_in_kms
If valid, return true. Else, return false
calculate_pizza_cost: Calculate pizza cost
Validate distance in kms
If valid,
Calculate pizza cost (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
Distance in kms Delivery Charge in km(in Rs)
For first 5 kms 5
For remaining 5 kms 7
Else, set pizza_cost to -1
Note: Perform case insensitive string comparison  
For testing:
Create objects of Pizzaservice and Doordelivery classes
Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
Display the details
'''
# class Customer:
#     def __init__(self):
#         self.__piza_quantity = None

#     def validate_quantity(self):
#         if self.__piza_quantity>=1 and self.__piza_quantity<=5:
#             return True
#         else:
#             return False

# class Pizzaservice:
#     def __init__(self):

# Google


class Customer:
    def validate_quantity(self, quantity):
        if quantity >= 1 and quantity <= 5:
            return True
        else:
            return False

class Pizzaservice:
    counter = 100
    
    def __init__(self, pizza_type, quantity, additional_topping):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.pizza_cost = 0
        self.service_id = ''
    
    def validate_pizza_type(self):
        if self.pizza_type.lower() == 'small' or self.pizza_type.lower() == 'medium':
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            if self.pizza_type.lower() == 'small':
                pizza_cost = self.quantity * 150
                if self.additional_topping:
                    pizza_cost += self.quantity * 35
            elif self.pizza_type.lower() == 'medium':
                pizza_cost = self.quantity * 200
                if self.additional_topping:
                    pizza_cost += self.quantity * 50
            self.pizza_cost = pizza_cost
            Pizzaservice.counter += 1
            self.service_id = self.pizza_type[0].upper() + str(Pizzaservice.counter)
        else:
            self.pizza_cost = -1
    
class Doordelivery(Pizzaservice):
    def __init__(self, pizza_type, quantity, additional_topping, distance_in_kms):
        super().__init__(pizza_type, quantity, additional_topping)
        self.distance_in_kms = distance_in_kms
    
    def validate_distance_in_kms(self):
        if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.distance_in_kms <= 5:
                    self.pizza_cost += self.distance_in_kms * 5
                else:
                    self.pizza_cost += 5 * 5
                    self.pizza_cost += (self.distance_in_kms - 5) * 7
        else:
            self.pizza_cost = -1

# Testing the program
pizza1 = Pizzaservice('small', 3, True)
pizza1.calculate_pizza_cost()
print(f"Service ID: {pizza1.service_id}\nPizza Type: {pizza1.pizza_type}\nQuantity: {pizza1.quantity}\nAdditional Topping: {pizza1.additional_topping}\nPizza Cost: {pizza1.pizza_cost}")

print("\n")

pizza2 = Doordelivery('medium', 2, False, 8)
pizza2.calculate_pizza_cost()
print(f"Service ID: {pizza2.service_id}\nPizza Type: {pizza2.pizza_type}\nQuantity: {pizza2.quantity}\nAdditional Topping: {pizza2.additional_topping}\nDistance in kms: {pizza2.distance_in_kms}\nPizza Cost: {pizza2.pizza_cost}")


























