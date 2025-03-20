# a = 'mynameisgautam'
# ## output =['my','name','is','gautam']

# b = list(str(a))
# print(b)

# char_list = ['m', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'g', 'a', 'u', 't', 'a', 'm']
# positions = [2, 6, 8, 14]  # Positions where words end (exclusive)

# result = []
# start = 0
# for end in positions:
#     result.append("".join(char_list[start:end]))
#     start = end
 
# print(result)


# why we use loop 
# type of loop 

#nested loops
#  call by refernce and call by value 
# call by object reference
# call by sharing
# call by copying

# Call by reference is a method of passing arguments to a function
#  where the actual memory address of the variable is passed.
# This means that changes made to the parameter inside 
# the function affect the original variable outside the function.

def modify_list(lst):
    lst.append(100)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 100]
# In this example, the function modify_list() takes a list as an argument.
# The function then appends an element to the list.
# Since lists are mutable, the changes made to the list inside the function affect the original list 
# outside the function.

# call by value
# Call by value is a method of passing arguments to a 
# function where the actual value of the variabl is passed.
# This means that changes made to the parameter inside the function do not affect the original variable outside th
# function.
def modify_list(lst):
    lst = [100, 200, 300]  # This line creates a new list
    return lst
    my_list = [1, 2, 3]
my_list = modify_list(my_list)
    # print(my_list)  # Output: [1, 2, 3]
    # In this example, the function modify_list() takes a list as an argument.