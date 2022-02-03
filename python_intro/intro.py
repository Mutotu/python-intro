# print("I am not dead yet!")
# my_variable = 5
# print(my_variable)

# my_bank_account = None

# if my_bank_account:
#     print(True)
# else:
#     print(False)
    
    
# print(3+3j)

# card = "whatsgoinonlol?"
# print(card)
# print(card.split(" "))
# print(card.split('o'))
# print('lol' in 'lol lolololol')

# print(len('lol'))



# My name is YOURFIRSTNAME YOURLASTNAME.
# my_name = 'Muto'
# last_name = 'lol'
# print('My nama is {} {}'.format(my_name, last_name))




# Make the above sentence a variable called my_name
# my_full_name  = my_name + ' ' + last_name
# print(my_full_name)

# Print the above sentence again by using the my_name variable

# Print the above sentence as an array, with each word being an array item.
# print(my_full_name.split(" "))
# Add a comment at the end of your array.
# info = 'My name is {}'.format(my_full_name)
# print('name' in info)
# Run code to determine if the above sentence contains the word "name"?

# How many characters are in the above sentence?
# print(len(info))
# print the above sentence with all uppercase letters
# print(info.upper())
# now all lowercase letters
# print(info.lower())
# now like it was originally

# replace your first name with initials
# print(info.replace("Muto lol", "replaced"))
# at what position does your first name appear?
# print(info.index('Muto'))
# permanently change the sentence so it has your initials instead of your full name.
# my_full_name=  'Permenantly changed'
# print(my_full_name)
# print(info)



# cat = {
#     "name":123
# }
# print(cat["name"])

# create a dictionary called "dog" and give it a "name", "weight in pounds" (integer or float), and "favorite food"

# dog = {
#     "name": "Wally",
#     "weight": 50,
#     "favorite_food":"Kebab"
# }


# your dog is just a puppy and has been growing rapidly. now change your dog's weight so it reflects an extra 2.1 pounds

# dog["weight"] = dog["weight"] + 2.1
# print(dog)

# EXERCISE 

# Create a dictionary called person with key-value pairs of name and age. 
# person = {"name":"Wally","age":21}
# def info(person):
#     if person["age"] == 16 or person["age"] == 17:
#         print("you can get your driver's license.")
#     elif person["age"]>= 18 and person["age"] <= 20:
#         print("This is {}, who is {}.{}, you can vote".format(person["name"],person["age"],person["name"] ))
#     elif person["age"] >= 21:
#         print("You can drink")
    
# info(person)


# Write a formatted string that takes the person's name, age, and returns a message specific to their age. If the person is 16 or 17, the message is "you can get your driver's license." If their age is 18, 19, or 20, the message is "you can register to vote." If the age is 21 or over, the message is, "you can drink now!"

# For example:
# This is Larry, who is 18 years old. Larry, you can register to vote.

# After you have gotten it to work with a selected age, change person's age to a different age group and see what it takes to make it work again.
# print(f"{person['name']} is lol")

# def ad(a,b):
#     return a + b

# print('2+3=', ad(2,3))

# tuple= ('Fireman', 'Firism')
# a,b = tuple


# print(a)

# a = "1,2,3"
# b,c,d = tuple(a.split(","))
# print(b,c,d)


# Try to write a program that prompts the user for the current temperature, and asks them whether they've entered a Celsius or Fahrenheit temperature. Have the program convert their temperature from the units they provided into the other units.

# (0°C × 9/5) + 32 = 32°F
#(32°F − 32) × 5/9 = 0°C


def ask_temp():
    current_temp = int(input("Enter temperature:"))
    temp_type = input("Enter temp in 'c' for celsius or 'f' for fahrenheit? ")
    cont = True
    while cont:
        if type(current_temp) == int:
            print('yes')
              
            if temp_type.lower()[0] == 'c':
                print((current_temp * 9/5) + 32 , ' in F')
                cont = False
            elif temp_type.lower()[0] == 'f':
                print((current_temp - 32) * 5/9, ' in C')
                cont = False
            else:
                print("Enter 'c' or 'f' only")  
                current_temp = int(input("Enter temperature: "))
                temp_type = input("Did you enter temp in 'c' for celsius or 'f' for fahrenheit? ")
                print(current_temp)
                print(temp_type)
    
            
        else:
            print('Only numbers')
            current_temp = int(input("Enter temperature: "))
            temp_type = input("Did you enter temp in 'c' for celsius or 'f' for fahrenheit? ")
            print(current_temp)
            print(temp_type)
          
    
print(ask_temp())