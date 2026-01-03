#Dictionaries
#1)All Possible operations.
# user_dictionary={
#     'username':'colacola',
#     'name':'kabir',
#     'age':18
# }
# print(user_dictionary)
# print(user_dictionary['name'])
# print(user_dictionary['age'])
# print(user_dictionary.keys())
# print(user_dictionary.values())
# print(user_dictionary.items())
# print(user_dictionary.get('name'))
#
# print(len(user_dictionary))
# user_dictionary['marriage']=False
# print(user_dictionary)

# user_dictionary.clear()
# print(user_dictionary)

# del user_dictionary

# for x,y in user_dictionary.items():
#     print(x,y)

# user_dictionary2=user_dictionary.copy()
# user_dictionary2.pop("age")
# print(user_dictionary2)

#2)ASSIGNMENT
# Dictionaries Assignment
# Based on the dictionary:
# my_vehicle = {
#     "model": "Ford",
#     "make": "Explorer",
#     "year": 2018,
#     "mileage": 40000
# }
# - Create a for loop to print all keys and values
# - Create a new variable vehicle2, which is a copy of my_vehicle
# - Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
# - Delete the mileage key and value from vehicle2
# - Print just the keys from vehicle2
# CODE:
# my_vehicle = {
#     "model": "Ford",
#     "make": "Explorer",
#     "year": 2018,
#     "mileage": 40000
# }
# for key, value in my_vehicle.items():
#     print(key, value)
# vehicle2=my_vehicle.copy()
# vehicle2['number_of_tires']=4
# del vehicle2['mileage']
# print(vehicle2.keys())