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

n=7
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("#" ,end = " ")
        else:
            print(" " , end=" ")
    print()

# n = 6  # Number of rows

# for i in range(n):
#     for j in range(i + 1):
#         if j == 0 or j == i or i == n - 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()  # Move to the next line

#
##
# #
#  #
# #
##
# 