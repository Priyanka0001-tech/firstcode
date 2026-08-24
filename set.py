#creating a set
fruits = {"apple", "banana", "mango", "orange"}

print(fruits)

   #empty set 
my_set = set()

print(my_set)

#duplicates in set
numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

#adding elements to a set
fruits = {"apple", "banana", "mango"}

fruits.add("orange")

print(fruits)


#adding multiple elements to a set
fruits = {"apple", "banana"}

fruits.update(["mango", "orange", "grapes"])

print(fruits)

#removing elements from a set
fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)