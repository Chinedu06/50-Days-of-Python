# Day 7: A String Range
# Write a function called string_range that takes a single number and 
# returns a string of its range. The string characters should be 
# separated by dots(.). For example, if you pass 6 as an argument, your
# function should return "0.1.2.3.4.5."
# Extra Challenge: Dictionary of Names
# You are given a list of names, and you are asked to write a code that 
# returns all the names that start with "S" (uppercase). Your code 
# should return a dictionary of all the names that start with S and how 
# many times they appear in the dictionary. Here is a list below:
# names = ["Joseph", "Nathan", "Sasha", "Kelly",
#  "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
# Your code should return: {"Sasha": 1, "Sera": 2}

def string_range(num):
    return '.'.join([str(i) for i in range(num)])
print(string_range(6))

def dictionary_of_names(lst):
    names = {}
    for name in lst:
        if name[0] == "S":
            names[name] = names.get(name, 0) + 1
    return names

names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
print(dictionary_of_names(names))

