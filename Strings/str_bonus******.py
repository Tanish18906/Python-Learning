'''
6. Bonus Questions
1. Write a program that counts how many vowels are in a given string.
2. Take a user input string and check if it is a palindrome (same forwards and
backwards).
'''


vowels = "aeiou"
name = input("enter a Word or Name: ")
count = 0


for i in name.lower():
    if i in vowels:
        count += 1
print("the number of vowels are :", count)        