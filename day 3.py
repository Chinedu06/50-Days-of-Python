# Day 3: Register Check
# Write a function called register_check that checks how many 
# students are in school. The function takes a dictionary as an argument. 
# If the student is in school, the dictionary says "yes." If the student is 
# not in school, the dictionary says "no." Your function should return the 
# number of students in school. Using the dictionary below, your 
# function should return 3.
# Extra Challenge: Lowercase Names
 
# names = ["kerry", "dickson", "John", "Mary", 
#  "carol", "Rose", "adam"]
# You are given a list of names above. This list is made up of names with
# lowercase and uppercase letters. Your task is to write a code that 
# will return a tuple of all the names in the list that only have
# lowercase letters. Your tuple should have names sorted 
# alphabetically in descending order. Using the list above, your code 
# should return:
# ('kerry', 'dickson', 'carol', 'adam')

def register_check(attendance):
    # Initialize a counter for students in school
    count = 0
    
    # Loop through each student's attendance status
    for status in attendance.values():
        if status == "yes":
            count += 1  # Increase count if the student is in school
    
    return count

students = {
    "John": "yes",
    "Emily": "no",
    "Steve": "yes",
    "Anna": "no",
    "Mike": "yes"
}

print(register_check(students))  # Should return 3


def lowercase_names(names):
    # Filter out names that are all lowercase
    lowercase_only = [name for name in names if name.islower()]
    
    # Sort the names in descending order
    lowercase_only.sort(reverse=True)
    
    # Convert to tuple and return
    return tuple(lowercase_only)

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

print(lowercase_names(names))  # Should return ('kerry', 'dickson', 'carol', 'adam')