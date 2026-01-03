#Functions
#1)Print is a inbuilt function
# print("Hello and welcome to functions!")

#2)Function basic working
# def my_name():              #Function declaration
#     print("I am Kabir")
# my_name()                   #Function calling

#3)Parameter
# def my_name(first_name, last_name):
#     print(f'My name is {first_name} {last_name}')
# my_name("Kabir","Roy")

#4)Another example
# def print_color_red():
#     color="Red"
#     print(color)
# color="blue"
# print(color)
# print_color_red()

#5)Explicit using the parametrs and arguments

# def print_numbers(highest_number,lowest_number):
#     print(highest_number)
#     print(lowest_number)
# print_numbers(1,2)
# print_numbers(lowest_number=2,highest_number=1)

#6)Multiply numbers
# def multiply(a,b):
#     return a*b;
# print(multiply(1,2))
# print(multiply(3,4))
# print(multiply(5,6))

#7)Print list of numbers
# def list_of_numbers(list_numbers):
#     for i in list_numbers:
#         print(i);
# list_of_numbers([1,2,3,4,5])

#8)Using Multiple Functions
# def buy_item(cost_of_item):
#     return cost_of_item + add_tax(cost_of_item)
# def add_tax(cost_of_item):
#     current_tax_rate=0.3;
#     return cost_of_item*current_tax_rate;
# print(buy_item(100))

#ASSIGNMENT

# def function(firstname,lastname,age):
#     dict={"firstname":firstname,"lastname":lastname,"age":age}
#     return dict
# print(function(firstname="John",lastname="Doe",age=30))