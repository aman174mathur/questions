# list0 = []
# list1 = [1,3,34,54,56,6]
# for i  in list1:
#     list0.append(i)
# print(list0)

# list0[3]=45
# print(list0)

# list0.pop(3)
# print(list0)

# diffrence bw remove and pop
# pop is used to remove the element by index
# remove is used to remove the element by value
# list0.remove(34)
# print(list0)


# list0.extend([1,23,3,3])
# print(list0)
# # index is used to find the index of the element
# print(list0.index(3))
# list0.index(3)
# print(list0)

# list0.append([11,12,13])
# print(list0)
# # reverse
# list0.reverse()
# print(list0)
# # sort
# list0.sort()
# print(list0)

# list0.remove([11,12,13])
# print(list0)

# diffrence bw list and tuplwe 
# list is mutable and tuple is immutab;e 
# list is defined by [] and tuple is defined by ()
# list is faster than tuple
# list is used for large data and tuple is used for small data
# list is used for dynamic data and tuple is used for static data

# tuple0 = (1,2,3,4,5,6)

# x=len(tuple0)
# print(x)    


# y = max(tuple0)
# print(y)

# z = sum(tuple0)
# print(z)

# a = tuple((tuple0))
# print(a)

# # swapping two elements from the list 
# list1 = [1,2,3,4,5,6]
# list2 = [7,8,9,10,11,12]
# a = list1[2]
# b = list2[2]
# c = list1[2] = b
# d = list2[2] = a
# print(list1)
# print(list2)

# x = (max(list1))
# print(x)

# # second highest number in the list
# list1 = [1,2,3,4,5,6]
# list1.sort()
# print(list1[-2])


# dictionary 
# key value pair
# dictionary is defined by {}
# dictionary is mutable
# dictionary is unordered
# dictionary is indexed

# use case of dictionary in real life
# 1. phonebook
# 2. dictionary
# 3. address book
# 4. contact list

# dictionary vs set 
# dictionary is key value pair and set is only value
# dictionary is defined by {} and set is defined by ()
# dictionary is mutable and set is immutable
# dictionary is unordered and set is ordered
# dictionary is indexed and set is not indexed

# what is a set
# set is a collection of unique elements
# set is defined by {}
# set is mutable
# set is unordered

# set functions 

# set1 = {1,3,5,7,9,10}
# set1.add(11)
# print(set1)
# x = set1.union()
# print(x)

# y = set1.intersection()
# print(y)

# z = set1.difference()
# print(z)

# total vovels in a string 
# string  = "hello world"
# count = 0
# list1 = []
# for i in string:
#     if i in "aeiou":
#         count = count + 1
#         list1.append(i)
# print(count)

# #  total vowels in a dictionary
# dict1 = { "name" : "hello world"}
# count = 0
# list1 = []
# list(map(lambda x: list1.append(x) if x in "aeiouAEIOU" else None, dict1["name"]))
# print(len(list1))


# check the consecutibe character ferwquency in a string
# str = "aabcdeef"
# list1 =[]
# count = 0
# freq = {}
# for i in str:
#     if i in list1:
#         count = count + 1
#         freq[i] = count
#     else:
#         count = 1
#         list1.append(i)
#         freq[i] = count
# print(freq)
# # access the values of the dictionary
# print(list(map(lambda x:freq[x], freq)))

# finding substring in a string
# str = "hello world"
# substring =[]
# sub2 = []
# freq = {}
# for i in str:
#     if i in substring:
#         freq[i] = freq[i] + 1
#     else:
#         freq[i] = 1
#         substring.append(i)
# print(freq)
# # access the key of the dictionary
# for key in freq:
#     sub2.append(key)    
# print(sub2)

# check if the string is palindrome or not

# str = "madam"
# start = []
# end= []
# for i in str:
#     start.append(i)
# for j in str[::-1]:
#     end.append(j)
# print(start)
# print(end)
# if start == end:
#     print("palindrome")
# else:
#     print("not palindrome") 

# #  checking valid parenthesis
# str = "{]}"
# list1 = []
# list2 = []
# for i in str:
#     if i in "{[(":
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list1)
# print(list2)
# if len(list1) == len(list2):
#     print("valid")
# else:
#     print("invalid")


# # count the ocuurances of a element in a list
# list1 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# # remove duplicates from the list
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)
# count the occurance of a element in a list
# freq = {}
# for i in list2:
#     count = 0
#     for j in list1:
#         if i == j:
#             count = count + 1
#             freq[i] = count
#         else:
#             freq[i] = count
# print(freq)
# # convert a dictionary to a list
# list3 = []
# for key in freq:
#     list3.append(key)
# print(list3)

# uppercasing half of the string 
# str = "hello world"
# list1 =[]
# list2 = []
# for i in str[:len(str)//2]:
#     list1.append(i.upper())
# for j in str[len(str)//2:]:
#     list2.append(j.upper())
# print(list1)
# print(list2)
# # how to convert a list to a string
# print("".join(list1))
# print("".join(list2))

# # remove substring from a string
# str = "hello world"
# list1 =[]
# list2 = []
# for i in str:
#     list1.append(i)
# for j in str:
#     if j in "aeiou":
#         list1.remove(j)
# print(list1)
# print("".join(list1))


# functions in python 
# lambda function : anonymous function that does not have a name 
# lambda function is defined by lambda keyword
# lambda function is used to create small functions
# lambda function can have any number of arguments but only one expression
# lambda function is used to perform small operations

# syntax of lambda function
# lambda arguments : expression

# example of lambda function
# x = lambda a : a + 10
# print(x(5))

# y= lambda argu1,arugu2 : argu1 * arugu2
# print(y(2,3))

# # map function : map function is used to apply a function to all the items in an input list
# # map function is defined by map keyword
# # map function returns a map object
# # map function is used to perform operations on list

# # syntax of map function
# # map(function,iterable)

# # example of map function
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = list(map(lambda x : x + 10, list1))
# print(list2)

# # can map function be used other than list?
# # yes map function can be used on list, tuple, set, dictionary and string

# # filter function : filter function is used to filter the elements from the list
# # filter function is defined by filter keyword

# # example of filter function
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = list(filter(lambda x:x%2==0,list1))
# print(list2)

# # reduce function : reduce function is used to reduce the elements of the list
# # reduce function is defined by reduce keyword
# # reduce function is used to perform operations on the list
# # reduce function is used to perform operations on the list and return a single value

# # example of reduce function
# from functools import reduce
# list1 = [1,2,3,4,5,6,7,8,9,10]
# x = reduce(lambda x,y:x+y,list1)
# print(x)


# why do we do list comprehension and dictionary comprehension
# list comprehension is used to perform operations on the list
# list comprehension is used to perform operations on the list and return a list 
# list comprehension is used to perform operations on the list and return a single value
# list comprehension is used to perform operations on the list and return a dictionary
# list comprehension is used to perform operations on the list and return a set

