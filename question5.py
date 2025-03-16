import math

# # -------------------
# def add(a,b):
#     return a+b
# result =add(10,30)
# print(result)

# # -------------------
# # positional argument 
# def add(a,b):
#     return a+b
# result = add(10,60)
# print(result)

# # -------------------
# # keyword arguments

# def greet(name , mesage):
#     return f"{mesage},{name}!"

# result = greet(mesage = "hello", name = "world")
# print(result)


# # -------------------
# # default argument (default value of an argument)
# def greet(name ,message = "hello"):
#     return f"{message},{name}!"
# result = greet("nernbienbi")
# print(result)

# # -------------------
# def square(x):
#     return x*x
# result = square(5)
# print(result)

# # variable length argument
# def sum_all(*args):        #args = multiple arguments of same type 
#     return sum(args)
# result = sum_all(1,2,3,4,5,6,7,8,9,10)
# print(result)

# def print_info(**kwargs):   #kwargs = multiple arguments of different type
#     for key , value in kwargs.items():
#         print(f"{key}:{value}")

# print_info(name = "Alice",age = 25, address = "USA")

# # lambda function
# square = lambda x:x*x
# result = square(5)
# print(result)


# # scope of a variable
# # local variable : variable that is declared inside a function 
# # global variable : variable that is declared outside a function

# # local
# def greet():
#     message = "hello"  #local variable
#     return message
# result = greet()
# # print(message) #error
# print(result)


# # global

# def my_func():
#     global x  #global variable
#     x = 10 
#     y = 100

# my_func()
# print(x)

# doc string : documentation string
# def add(a, b):
#     """
#     This function adds two numbers and returns the result.
#     """
#     return a + b

# result = add(10,20)
# print(result)
# # Access the docstring
# print(add.__doc__)

# # recursive func : function that calls itself
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1) #recursive call
# result = factorial(5)
# print(result)

# # 1. Finding LCM & HCF of two & three numbers

# def finding_hcf(a,b):
#     while b:
#         a,b = b,a%b
#     return a 

# def finding_lcm(a,b):
#     return (a*b)//finding_hcf(a,b)

# num1 , num2 = 12,13
# hcf = finding_hcf(num1,num2)
# lcm = finding_lcm(num1,num2)

# print(hcf)
# print(lcm)

# fibonnaci series using func

# valid paraenthis 

#first class functions and high order functions vs high order functions
