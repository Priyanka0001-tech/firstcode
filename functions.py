#simple function
def greet():
    print("Hello, Welcome to Python!")

greet()

#function with parameters
def greet(name):
    print("Hello,", name)

greet("Priyanka")
greet("piya")

#function with return value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

#function with default parameter
def greet(name="Guest"):
    print("Welcome,", name)

greet()
greet("Priyanka")

#function with variable number of arguments
def greet(*names):
    for name in names:
        print("Hello,", name)

greet("Priyanka")
greet("piya")
greet("Rahul", "Sneha")

#function with keyword arguments
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
greet(name="Priyanka")
greet(name="piya")
greet(name="Rahul", age=25)

#function with docstring
def greet(name):
    """This function greets the person with the given name."""
    print("Hello,", name)

greet("Priyanka")
print(greet.__doc__)