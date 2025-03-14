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

# for i in range(num):
#     for j in range(i+1):
#         if j == 0 or j ==i or i==num -1:
#             print("*" , end = " ")
#         else:
#             print(" ", end = " ")
#     print() 
# for k in range(num):
#     for l in range(num-k-1):
#         if l == 0 or l == 
#         else:
#             print(" ", end = " ")
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