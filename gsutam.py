a = 'mynameisgautam'
## output =['my','name','is','gautam']

b = list(str(a))
print(b)

char_list = ['m', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'g', 'a', 'u', 't', 'a', 'm']
positions = [2, 6, 8, 14]  # Positions where words end (exclusive)

result = []
start = 0
for end in positions:
    result.append("".join(char_list[start:end]))
    start = end
 
print(result)