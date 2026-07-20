#creating a list
fruits = ["Apple", "Banana", "Mango"]

print(fruits)

#accessing list elements
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])     # First element
print(fruits[1])     # Second element
print(fruits[-1])    # Last element

#list slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

#add elements to a list
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

#insert an element
fruits = ["Apple", "Mango"]

fruits.insert(0, "Banana")

print(fruits)

#remove an element
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

#remove last element
fruits = ["Apple", "Banana", "Mango"]

removed = fruits.pop()

print("Removed:", removed)
print(fruits)

#update an element
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

#loop through a list
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

#check if an element exists 
fruits = ["Apple", "Banana", "Mango"]

if "Banana" in fruits:
    print("Banana is available")


# find the length of a list
fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))

#sort a list
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)

#reverse a list
numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)

#list concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)

#list comprehension
squares = [x ** 2 for x in range(1, 6)]

print(squares)

#find minimum and maximum values 
numbers = [10, 25, 5, 40, 15]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

#sum of elements in a list
numbers = [10, 20, 30, 40]

print("Sum =", sum(numbers))

#count occurrences of an element in a list
numbers = [1, 2, 2, 3, 2, 4]

print(numbers.count(2))

#copy a list
list1 = [10, 20, 30]

list2 = list1.copy()

print(list2)

"""student marks """
marks = [85, 90, 78, 88, 92]

print("Marks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))