#for loop 
for i in range(1, 6):
    print(i)

#while loop
count = 1
while count <= 5:
    print(count)
    count += 1

#nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"Row {i}, Column {j}")

#loop with break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)    

#loop with continue statement
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)    

#loop with else statement
for i in range(1, 6):   
    print(i)    
else:
    print("Loop completed successfully.")   

#loop with pass statement
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)

#loop with nested if statement
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

#loop with nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")    

#loop with nested while loop
count1 = 1
while count1 <= 3:
    count2 = 1
    while count2 <= 3:
        print(f"count1: {count1}, count2: {count2}")
        count2 += 1
    count1 += 1

#loop with nested if-else statement
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")    
