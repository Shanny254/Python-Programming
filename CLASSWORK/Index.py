## Dictionary creation
students={
    "name": "Sharlyne",
    "age": "23",
    "gender":"Female",
    "is_student": True,
    "courses": ["Math","English","Kiswahili"],
    
    "my_name": {
        "first_name": "Shanny",
        "last_name": "Nyaboke"
    }
}
students["height"]= 2.56

print(students["height"])
print(students)
print(students["courses"][2])


# Creating a set with various data types
students_set = {42, 3.14, False, "Hello", (1, 2, 3)}
print(students_set)
print(type(students_set))


students_set = {
    "Sharlyne", 23, "Female", True, 2.56, 
    ("Math", "English", "Kiswahili"), 
    frozenset({"first_name": "Shanny", "last_name": "Nyaboke"}.items())
}
print(students_set)
