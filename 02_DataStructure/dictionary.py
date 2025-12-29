# it is just like hashmap in java
# Mutable , Duplicates(key - unique , value  might be different) , ordered , Heterogeneus
# we can only apply CRUD operation on values but not on the keys after creation

# Empty dictionary (not a set or tuple)
x = {}  
print(type(x))  # <class 'dict'>

# Dictionary with key-value pairs (heterogeneous keys/values allowed)
student = {
    "name": "Krishna Garg",
    "rollNumber": 2215000931,
    "marks": [85, 92, 78],      # List as value
    "subjects": {"math": 95}    # Dict as value
}
print(type(student))
# <class 'dict'>

# ADD NEW KEY-VALUE PAIR: If key doesn't exist, Python automatically creates it
# No need to check existence beforehand - dictionary grows dynamically
student["address"] = "MadhuNagar , Agra" 
# READ: Access value using key (KeyError if missing)
print(student["name"])        # Krishna Garg
print(student.get("age", "N/A"))  # N/A (safe access)

# CREATE/UPDATE: Add or modify value
student["email"] = "krishna@example.com"      # New key-value
student["marks"] = [90, 95, 88]              # Update existing

# DELETE: Remove key-value pair
del student["rollNumber"]                     # Removes entry
# student.pop("name")                        # Alternative

print(student)
# {'name': 'Krishna Garg', 'marks': [90, 95, 88], 
#  'subjects': {'math': 95}, 'email': 'krishna@example.com'}

# Length
print(len(student))  # 4

# Check key existence
print("name" in student)  # True

# Keys, Values, Items views
print(student.keys())    # dict_keys(['name', 'marks', ...])
print(student.values())  # dict_values(['Krishna Garg', [90, 95, 88], ...])
print(student.items())   # dict_items([('name', 'Krishna Garg'), ...])

# Copy (shallow)
copy_student = student.copy()


# Traversing in the Dictinary

for i in student:
  print(f"the key : values are {i} : {student[i]} ")
  
help(dict)


# deep Copy
# shalow Copy 