#Print the multiplication table of a number (entered by user)

num = int(input("Enter the Number:"))

for i in range(1,11,1):
    print(num,"x", i, "=", num*i)