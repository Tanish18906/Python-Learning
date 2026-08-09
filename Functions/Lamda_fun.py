'''
3. Lambda Functions
1. Write a lambda function that adds two numbers and test it.
2. Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
their squares.
'''

add = lambda x,y: x + y
print(add(10,60))

num = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, num))
print(square)
