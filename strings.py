#string 
name = "Priyanka"
print(name)

#accessing characters in a string
name = "Priyanka"
print(name[0])  # P
print(name[1])  # r 
print(name[2])  # i

#string slicing
name = "Priyanka"
print(name[0:3])  # Pri
print(name[3:6])  # yan
print(name[6:9])  # ka

#string concatenation
first_name = "Priyanka"
last_name = "Sharma"
full_name = first_name + " " + last_name
print(full_name)  

#string repetition
name = "Priyanka"
print(name * 3) 

#uppercase and lowercase
name = "Priyanka"
print(name.upper())  
print(name.lower())  

#removing extra spaces
name = "   Priyanka   "
print(name.strip())  

#replace a word in a string
name = "Priyanka Sharma"
print(name.replace("Sharma", "Bhardwaj"))

#finding a word in a string
name = "Priyanka Sharma"
print(name.find("Sharma"))  # returns the index of the first occurrence of "Sharma"


#check if a word is in a string
text = "Python Programming"

if "Python" in text:
    print("Found")
else:
    print("Not Found")

#splitting a string
text = "Apple,Banana,Mango"

fruits = text.split(",")

print(fruits)

#join strings
fruits = ["Apple", "Banana", "Mango"]

text = ", ".join(fruits)

print(text)


