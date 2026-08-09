'''
. Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:
1. Both length and width
2. Only length (use default width)

'''

def area( length, width = 10):
    return length * width

print(area(3, 20)) # calling both length and width
print(area(3)) # calling only lenght
