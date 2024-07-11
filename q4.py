username = str(input("Enter your Name:"))

if (len(username) < 10):
    print("Your UserName contain less than 10 character:", username)
else:
    print("Your UserName contain greater than or equal to 10 character:", username)