a1 = int(input("Enter the No:"))
a2 = int(input("Enter the No:"))
a3 = int(input("Enter the No:"))
a4 = int(input("Enter the No:"))

if (a1>a2 and a1>a3 and a1>a4):
    print("A1 is greater")
elif (a2>a1 and a2>a3 and a2>a4):
    print("A2 is greater")
elif (a3>a1 and a3>a2 and a3>a4):
    print("A3 is greater")
else:
    print("A4 is greater")