name = "Jayavarshini"
print(name)

password=""
while  password != "DOB":
     password = input("enter you password")
print("Login successfully")

marks1 = int(input("Enter your TAMIL marks: "))
if marks1 >= 90:
    print("DISTINCTION")
elif marks1 >= 75:
    print("FIRST CLASS")
elif marks1 >= 50:
    print("SECOND CLASS")
elif marks1 >= 35:
    print("THIRD CLASS")
else:
    print("SORRY : FAILED")

marks2 = int(input("Enter your ENGLISH marks: "))
if marks2 >= 90:
    print("DISTINCTION")
elif marks2 >= 75:
    print("FIRST CLASS")
elif marks2 >= 50:
    print("SECOND CLASS")
elif marks2 >= 35:
    print("THIRD CLASS")
else:
    print("SORRY : FAILED")

marks3 = int(input("Enter your MATHS marks: "))
if marks3 >= 90:
    print("DISTINCTION")
elif marks3 >= 75:
    print("FIRST CLASS")
elif marks3 >= 50:
    print("SECOND CLASS")
elif marks3 >= 35:
    print("THIRD CLASS")
else:
    print("SORRY : FAILED")

marks4 = int(input("Enter your SCIENCE marks: "))
if marks4 >= 90:
    print("DISTINCTION")
elif marks4 >= 75:
    print("FIRST CLASS")
elif marks4 >= 50:
    print("SECOND CLASS")
elif marks4 >= 35:
    print("THIRD CLASS")
else:
    print("SORRY : FAILED")
marks5 = int(input("Enter your SOCIAL marks: "))
if marks5 >= 90:
    print("DISTINCTION")
elif marks5 >= 75:
    print("FIRST CLASS")
elif marks5 >= 50:
    print("SECOND CLASS")
elif marks5 >= 35:
    print("THIRD CLASS")
else:
    print("SORRY : FAILED")

Total= marks1 + marks2 + marks3 + marks4 + marks5
print("Total", Total)
if Total >= 150:
    print("PASS")
else:
    print(FAILED)







