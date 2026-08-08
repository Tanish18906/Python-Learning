'''. Take a user input string and check if it is a palindrome (same forwards and
backwards).'''


text = str(input("enter the word: "))

palin = text[::-1]

if text == palin:
    print("the Word is Palindrome")

else:
    print("the word is NOT palindrome")



