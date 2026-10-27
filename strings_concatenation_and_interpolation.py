# Concatenation
my_str_1 = 'Hello'
my_str_2 = 'World'

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# Repeating Strings
sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) # hahaha

# Concenating Strings with Numbers
name = 'John Doe'
age = 26

#name_and_age = name + ' ' + str(age)

#name_and_age = name # Start with the name
#name_and_age += str(age) # Append the age as string
#print(name_and_age) # John Doe26

# Interpolation
num1 = 5
num2 = 6
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 6 is 11