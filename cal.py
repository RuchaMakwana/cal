print("Mini Calculator")

num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))

print("Press1 for Addition \nPress2 for Substraction \nPress3 for Multiplication \nPress4 for Divison")

choice = int(input("Enter Your Choice From 1 To 4:"))
if choice == 1:
    print(num1 + num2)
elif choice == 2 :
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("Invalid Input")