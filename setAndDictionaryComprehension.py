#Sets

#create a set with the characters of the word
my_list = {char for char in 'hello'}

#Create a set with numbers from 0-100
my_list2 = {num for num in range(0,100)}

#Create a set with the squares of numbers between 0-100
my_list3 = {num**2 for num in range(0,100)} 

#Create a set with only the even squares of numbers between 0-100
my_list4 = {num**2 for num in range(0,100) if num % 2 == 0}

print(my_list)
print()
print(my_list2)
print()
print(my_list3)
print()
print(my_list4)
print()

#Dictionary

simple_dict = {
  'a': 1,
  'b': 2
}

#Create a new Dictionary where the value is squared
my_dict = {key:value**2 for key, value in simple_dict.items()}

#Create a new Dictionary where the value is only added if when the value is squared it returns an even number
my_dict1 = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}

print(simple_dict)
print()
print(my_dict)

print()
print(my_dict1)

#Create a dictionary that takes the number from the list as the key and times it by 2 for the value
my_dict2 = {num:num*2 for num in [1,2,3]}

print()
print(my_dict2)