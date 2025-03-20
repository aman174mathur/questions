# n=4
# a=1
# for i in range(n):
#     for k in range(n-i):
#         print(" " , end =" ")
#     for l in range(i+1):
#         print( , end = "  ")
#     print()

# def print_floyds_triangle(rows):
#     """Prints Floyd's triangle with the given number of rows."""
#     number = 1  # Start with 1
#     for i in range(1, rows + 1):  # Iterate through rows
#         row_str = ""
#         for j in range(i):  # Iterate through columns in the current row
#             row_str += str(number) + " "
#             number += 1  # Increment the number
#         print(row_str.strip())

# # Example usage:
# print_floyds_triangle(5)  # Prints Floyd's triangle with 5 rows.
# print("\nFloyd's triangle with 8 rows:\n")
# print_floyds_triangle(8)


# rows = 4
# start_with_one = True
# for i in range(rows):
#     num_digits = i * 2 + 1 if i < 2 else i + 2  # Calculate number of digits per row
#     current_digit = 1 if start_with_one else 0
#     row_str = ""
#     for j in range(num_digits):
#         row_str += str(current_digit) + " "
#         current_digit = 1 - current_digit  # Toggle between 0 and 1
#     print(row_str.strip())
#     start_with_one = not start_with_one  # Toggle starting digit for next row

# # Example to show different number of rows
# print("\nExample with 6 rows:\n")
# rows = 6
# start_with_one = True
# for i in range(rows):
#     num_digits = i * 2 + 1 if i < 2 else i + 2
#     current_digit = 1 if start_with_one else 0
#     row_str = ""
#     for j in range(num_digits):
#         row_str += str(current_digit) + " "
#         current_digit = 1 - current_digit
#     print(row_str.strip())
#     start_with_one = not start_with_one


# n=4
# for i in range(n):
#     for j in range(i+1):
#             print((i+j)%2, end=" ")
#     print()

# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end= " ")
#     for k in range(n-i-1):
#         print(" " , end = " ")
#     for l in range(n-i-1):
#         print(" " , end =" ")
#     for f in range(i+1):
#         print(j+1 , end = " ")
#     print()


# n=5
# a=1
# for i in range(n):
#     for j in range(i+1):
#         print(a, end = " ")
#         a+=1
#     print()


# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i), end = " ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" " , end = "")
#     for k in range(i+1):
#         print(chr(65+k) , end = " ")
#     for k in range(i-1,-1,-1):
#         print(chr(65+k) , end = " ")
#     print()

