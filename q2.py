Math = int(input("Enter the No:"))
Science = int(input("Enter the No:"))
Urdu = int(input("Enter the No:"))

avg = (Math + Science + Urdu) / 300
percentage = avg * 100

if (percentage >= 40):
    print( "Student has Pass:",percentage,"%")
else:
    print("Student has Failed", percentage,"%")
