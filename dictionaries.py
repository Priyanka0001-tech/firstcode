#dictionary
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

print(student)

#accessing dictionary elements
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

print(student["name"])
print(student["age"])
print(student["course"])


#using get() method to access dictionary elements
student = {
    "name": "Priyanka",
    "age": 21
}

print(student.get("name"))
print(student.get("course", "Not Found"))

#adding new key-value pairs to a dictionary

student = {
    "name": "Priyanka",
    "age": 21
}

student["course"] = "BCA"

print(student)


#update a value
student = {
    "name": "Priyanka",
    "age": 21
}

student["age"] = 22

print(student)

#reove an item from a dictionary
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

student.pop("age")

print(student)

#removing the last inserted item from a dictionary
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

student.popitem()

print(student)

#deleting a key-value pair from a dictionary
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

del student["course"]

print(student)

#loop through keys
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

for key in student:
    print(key)

#loop through values
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

for value in student.values():
    print(value)

#loop through key-value pairs
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

for key, value in student.items():
    print(key, ":", value)

#check if a key exists
student = {
    "name": "Priyanka",
    "age": 21
}

if "age" in student:
    print("Age is available")

#dictionary length
student = {
    "name": "Priyanka",
    "age": 21,
    "course": "BCA"
}

print(len(student))

#copying a dictionary
student = {
    "name": "Priyanka",
    "age": 21
}

new_student = student.copy()

print(new_student)

#nested dictionary
students = {
    "student1": {
        "name": "Priyanka",
        "marks": 90
    },
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students["student1"]["name"])

#dictionary comprehension
squares = {x: x*x for x in range(1, 6)}

print(squares)

#merging two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = dict1 | dict2   # Python 3.9+

print(result)

#clearing a dictionary
student = {
    "name": "Priyanka",
    "age": 21
}

student.clear()

print(student)
