#creating a tuple
fruits = ("Apple", "Banana", "Mango")

print(fruits)

#accessing tuple elements
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])    # First element
print(fruits[2])    # Third element
print(fruits[-1])   # Last element

#tuple slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
 
#loop through a tuple
fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)

#finding the length of a tuple
fruits = ("Apple", "Banana", "Mango")

print(len(fruits))

#checking if an element exists in a tuple
fruits = ("Apple", "Banana", "Mango")

if "Banana" in fruits:
    print("Banana is available")

#counting the occurrences of an element in a tuple
numbers = (1, 2, 2, 3, 2, 4)

print(numbers.count(2))

#finding the index of an element in a tuple
fruits = ("Apple", "Banana", "Mango")

print(fruits.index("Banana"))


#tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

#tuple repetition
numbers = (1, 2)

print(numbers * 3)