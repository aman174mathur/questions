for i in range(1,12):
    print(i)


# sum of no from 1 to 10 
sum = 0 
for i in range(1,12):
    sum += i
print(sum)  # output: 66    

n= 5 
for i in range(n):
    for j in range(1, i+1):
        print( j , end = " ")
    print()

for i in range(5):
    for j in range(i+1):
        print("*" , end= " ")
    print()

list1= [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda x:x**2 , list1))
print(square)  

another_sq= [i**2 for i in range(1,23)]
print(another_sq)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = [num for num in numbers if num%2!=0]
print(even_num)  # Output: [2, 4, 6, 8

original_dict = {'a': 1, 'b': 2, 'c': 3}

double_val = {key:value*2 for key,value in original_dict.items()}
print(double_val)

original_dict = {'a': 1, 'b': 6, 'c': 3, 'd': 7}
filtered_val = {key:value for key ,value in original_dict.items() if value>5}
print(filtered_val)

# Compare the performance of using a for 
# loop versus list comprehension to create a list
# of squares of numbers from 1 to 1000.


#  diff bw for loop and while loop

#  for loop are used when there are range of value and while 
# loop are used when there is no range of values 
#  for loop are used when we know the number of iteration
#  while loop are used when we don't know the number of iteration
#  for loop are used when we need to iterate over a sequence
#  while loop are used when we need to iterate over a condition
#  for loop are used when we need to iterate over a collection
#  while loop are used when we need to iterate over a condition 




# how does break and continue work in python
# break is used to terminate the loop
# continue is used to skip the current iteration of the loop
#  break and continue are used to control the flow of the loop
#  break and continue are used to skip the current iteration of the loop

for i in range(1,11):
    if i == 5:
        print(i)
        break

for i in range(1,11):
    if i == 5:
        print(i)
        continue
    print(i)


#   How can you iterate over a list and modify its elements at the same time?
 
list1 = [ 1, 2, 3, 4, 5]
list2 = []
for i in range(len(list1)):
   if  list1[i] % 2 == 0:
     list2.append(list1[i])
print(list2)

list1 = [1, 2, 3, 4, 5]
list2 = [x for x in list1 if  x % 2 == 0]
print(list2)

# What are generator expressions, 
# and how are they different from normal loops?

# genrators are functions that can be
# iterated upon, but do not compute their values until needed
#  they are used to generate a sequence of results,
#  rather than computing them all at once

# for ex 
list1 = [1, 2, 3, 4, 5]
# list2 = [x for x in list1 if x % 2 == 0 ]
# print(list2)
list2 = (x for x in list1 if x % 2 == 0 )
print(list2)
print(next (list2))
print(next (list2))

# How can you iterate through multiple lists 
# at the same time using loops?
#  you can use the zip() function to 
# iterate through multiple lists at the same time
#  the zip() function returns an iterator of tuples
#  where the first item in each passed iterator is
# for example
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for i, j in zip(list1, list2):
    print(i, j)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
for i, j, k in zip(list1, list2, list3):
    print(i, j, k)


dictionary1= {'a': 1, 'b': 2, 'c': 3}
# dictionary2 = {key:values for key,values in dictionary1.keys() if key != 'b', dictionary1.values()  if values != 2 }
for value in dictionary1.values():
    print(value)  # prints key value pairs



# for right angled triangled 
n=5
for i in range(n):
    for j in range(i+1):
        print("&" , end = " ")
    print()
    
# pyramid

n=6
for i in range(n):
    for j in range(n-i):
        print(" ", end = " ")
    for k in range(i):
        print("*", end = " ")
    for l in range(i-1):
        print("*", end = " ")
    print()


# Can you write a Python program to print
#  a number pattern where each row contains the row number?

n=5
# for i in range(n):
#     for j in range(i):
#         print(i+1, end = " ")
#     print()

# inverted pyramid using numbers -------------------------------------->

# n=6
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(n-i):
#         print( 1+i, end=" ")
#     for l in range (n-i-1):
#         print(1+i, end=" ")
#     print()


# What is the approach to printing a Pascal’s Triangle using loops?

# def print_pascal_triangle(rows):
#     trisngle = [[1]*(i+1) for  i in range(rows)]

#     for i in range(2,rows):
#         for j in range(1,i):
#             trisngle[i][j] = trisngle[i-1][j-1] + trisngle[i-1][j]
#         return trisngle
    
# for row in print_pascal_triangle(5):
#     print(" "*(5- len(row)), " ".join(map(str, row)))
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
