# This exercise is to find a specific character

# Please make user to input their email address

# Please validate the input, if the input is correct, end the program
# If the input is incorrect, tell the user to input again

x = input("Please input your email: ")
while x.find("@") == -1:
    print("Your input is not correct, try again")
    x = input()
print("Your input is correct")