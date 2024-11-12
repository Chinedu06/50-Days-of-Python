# Day 5: My Discount
# Create a function called my_discount. The function takes no 
# arguments but asks the user to input the price and the discount
# (percentage) of the product. Once the user inputs the price and 
# discount, it calculates the price after the discount. The function 
# should return the price after the discount. For example, if the user 
# enters 150 as the price and 15% as the discount, your function should 
# return 127.5.
# Extra Challenge: Tuple of Student Sex
# You work for a school, and your boss wants to know how many female 
# and male students are enrolled in the school. The school has saved the 
# students on a list. Your task is to write a code that will count how many 
# males and females are in the list. Here is a list below:
# students = ['Male', 'Female', 'female', 'male', 'male', 'male',
# 'female', 'male', 'Female', 'Male', 'Female', 
# 'Male', 'female']
# Your code should return a list of tuples. The list above should return:
# [("Male", 7), ("female", 6)].

def my_discount():
    # Get price and discount from user input
    price = float(input("Enter the price of the product: "))
    discount = float(input("Enter the discount percentage: "))
    
    # Calculate the discount amount
    discount_amount = (discount / 100) * price
    
    # Calculate the final price after discount
    final_price = price - discount_amount
    
    return final_price

# Call the function and print the result
discounted_price = my_discount()
print("Price after discount:", discounted_price)


def count_student_sex(students):
    # Normalize cases to make counting easier
    normalized_students = [student.capitalize() for student in students]
    
    # Count occurrences of each gender
    male_count = normalized_students.count("Male")
    female_count = normalized_students.count("Female")
    
    # Return the result as a list of tuples
    return [("Male", male_count), ("female", female_count)]

students = [
    'Male', 'Female', 'female', 'male', 'male', 'male',
    'female', 'male', 'Female', 'Male', 'Female', 
    'Male', 'female'
]

print(count_student_sex(students))  # Should return [("Male", 7), ("female", 6)]
