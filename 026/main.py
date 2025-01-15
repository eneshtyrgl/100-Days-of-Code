# Create Lists using List Comprehension


#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

#List Comprehension
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

#String as List
name = "Enes"
letters_list = [letter for letter in name]
print(letters_list)

#Range as List
double_list = [num*2 for num in range(1,5)]
print(double_list)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names_uppercase = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names_uppercase)

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    name: grade
    for (name, grade) in student_grades.items() if grade >= 60
}
print(passed_students)


# Iterate over

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)

# Looping through a data frame
for (key, value) in student_data_frame.items():
    print(value)

# Looping through rows of a data frame and iterrows() method
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    if row["student"] == "Lily":
        print(f"Lily's Score: {row.score}")

        student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}