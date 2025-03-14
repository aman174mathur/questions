# # Example 1: Program to print half pyramid using *

# for i in range(5):
#     for j in range(i+1):
#         print("*", end= " ")
#     print()

# # Example 2: Program to print half pyramid a using numbers

# for i in range(5):
#     for j in range(i+1):
#         print(j, end=" ")
#     print()

# # Example 3: Program to print half pyramid using alphabets
# ascii_value = 65
# for i in range(5):
#     for j in range(i+1):
#         alphabet = chr(ascii_value)
#         print(alphabet , end=" ")
#     ascii_value+=1
#     print()

# # Example 4: Inverted half pyramid using *
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*" , end=" ")
#     print()

# Example 6: Program to print full pyramid using *

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" " , end = " " )
    
#     for k in range(i+1-1):
#         print("*" , end = " ")

#     for l in range(i+1):
#         print("*" , end= " ")
#     print()

# Example 7: Full Pyramid of Numbers
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" " , end = " " )
    
#     for k in range(i,2*i):
#         print(k, end = " ")

#     for l in range(2*i - 2,i-1,-1):
#         print(l  , end= " ")
#     print()

# n=7
# for i in range(n):
#     for j in range(i+1):
#         if j==0 or j==i or i==n-1:
#             print("#" ,end = " ")
#         else:
#             print(" " , end=" ")
#     print()

# n = 6  # Number of rows

# for i in range(n):
#     for j in range(i + 1):
#         if j == 0 or j == i or i == n - 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()  # Move to the next line

# n = 6  # Number of rows

# for i in range(0,4):
#     for j in range(i + 1):
#         if j == 0 or j == i or i == n - 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#         for k in range(n-i):
#             if j == 0 or j == i or i == n - 1:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()  # Move to the next line

# n= 7
# for i in range(n):
#     for j in range(i+1):
#         print(" " , end = " ")
#     for k in range(
#     for l in range(n-i):
#         if i==2 or i==4 or i==6:
#             print("*" , end = " ")
#         print()

#  ******

#  *   *

#  * *

#   *


# num = int(input("Enter the number of rows: "))

# # for i in range(num):
# #     for j in range(i+1):
# #         if j == 0 or j ==i or i==num -1:
# #             print("*" , end = " ")
# #         else:
# #             print(" ", end = " ")
# #     print() 
# for k in range(num):
#     for l in range(num-k-1):
#         if l == 0 or l == num - k - 1 or k == num - 1:
#             print("*" , end = " ")
#         else:
#             print("&", end = " ")
#     print()

# .program to find the frequency of the substring 

# str = "ababa"
# # output :{'a': 3, 'b': 2 , "ab":2 , "ba":2 , "aba":1 , "bab":1 , "ababa": 1 , "baba":1 } 
# freq = {}
# list1 =[]
# for i in range(len(str)):
#     for j in range(i+1,len(str)+1):
#         list1.append(str[i:j])
# for i in list1:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1
# print(freq)


# num = int(input('Enter the number: '))

# # Upper part (increasing triangle)
# for i in range(0, num):
#     for j in range(0, i + 1):
#         if j == 0 or j == i :
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

# # Lower part (decreasing triangle)
# for i in range(1, num):
#     for j in range(0, num - i):
#         if j == 0 or j == num - i - 1 or i == num - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

# n=6
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end = " ")
#     for k in range(n-i):
#         if k==1 or i==0 :
#             print("*" , end = " ")
#     print()

# 1234
# 234
# 34
# 4

# n = 4  # Number of rows
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         print(j, end="")
#     print()


# n=4
# for i in range(n):
#     for j in range(i+1-1):
#         print("  ", end = "")
#     for k in range(i+1,n+1):
#         print(k, end = "  ")
#     print()

# # pyramid
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end = " ")
#     for k in range(i+1):
#         print("*", end = " ")
#     for l in range(i+1-1):
#         print("*", end = " ")
#     print()

# hollow pyramid

# n = 5
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for k in range(i + 1):
#         if k == 0 or i==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for l in range(i):
#         if l == i - 1 or i==n-1 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# diamond shape

# n=5 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end = " ")
#     for k in range(i+1):
#         print("*", end = " ")
#     for l in range(i+1-1):
#         print("*", end = " ")
#     print()
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ", end = " ")
#     for k in range(n-i-1):
#         print("*", end = " ")
#     for l in range(n-i-2):
#         print("*", end = " ")
#     print()

# square 

# for i in range(6):
#     for j in range(6):
#         if j==0 or j==5 or i==0 or i==5:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# number pyramid 

# n=5 
# for i in range(1,n):
#     for j in range(n-i-1):
#         print("", end = " ")
#     for k in range(i):
#         print(i, end = " ")
#     print()
    # Pattern:
    #     1
    #    2 2
    #   3 3 3
    #  4 4 4 4

# n = 4  # Number of rows
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(i):
#         print(i, end=" ")
#     print()

    # n = 4  # Number of rows
    # for i in range(1, n + 1):
    #     for j in range(i):
    #         print(i, end="")
    #     print()


# Pattern:
# 1
# 23
# 456

n = 4  # Number of rows
num = 0  # Starting number
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# how to get substring from a string
str = "ababa"
substr = []
dic1 = {}
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        substr.append(str[i:j])

for i in substr:
    if i in dic1:
        dic1[i] +=1
    else:
        dic1[i] = 1 
print(substr)
print(dic1)

# character freq from a string

str = "ababa"
list1 = []
for i in str:
    list1.append(i)
freq = {}
for i in list1:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
print(freq)