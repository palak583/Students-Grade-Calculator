print(input("Enter student name:"))
num1 = float(input("Enter Maths marks:"))
num2 = float(input("Enter Physics marks:"))
num3 = float(input("Enter Chemistry marks:"))
num4 = float(input("Enter English marks:"))
num5 = float(input("Enter CS marks:"))

total = num1+num2+num3+num4+num5 
Percentage = total / 5

if Percentage >= 90:  
     print("Grade A:")
elif Percentage >= 85:
    print("Grade B:")
elif Percentage >= 75:
    print("Grade C:")
elif Percentage >= 65:
    print("Grade D:")
else:
    print("Grade F")

print("Total:",total)
print("Percentage:", Percentage)

