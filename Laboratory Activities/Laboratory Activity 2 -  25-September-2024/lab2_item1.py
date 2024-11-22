user = int(input("Enter an integer: "))
newuser = str(user)
usercopy = newuser[::-1]
if newuser == usercopy:
    print("Palindrome")
else:
    print("Not a palindrome")
