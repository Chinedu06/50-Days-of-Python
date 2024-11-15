# Day 6: User Name Generator
# Write a function called user_name that generates a username from 
# the user’s email. The code should ask the user to input an email, and 
# the code should return everything before the @ sign as their user 
# name. For example, if someone enters ben@gmail.com, the code 
# should return ben as their user name.


def user_name():
    email = input("Enter your Email:")
    return f'Your username is {email.split("@")[0]}'
print(user_name())

# Extra Challenge: Zero Both Ends
# Write a function called zeroed code that takes a list of numbers as an 
# argument. The code should zero (0) the first and last number in the 
# list. For example, if the input is [2, 5, 7, 8, 9], your code should 
# return [0, 5, 7, 8, 0].

def zeroed_code(lst):
    lst[0] = 0
    lst[-1] = 0
    return lst
print(zeroed_code([2, 5, 7, 8, 9]))