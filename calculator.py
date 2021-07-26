num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))


operation = int(input("Choose Operation \n 1.Addition \n 2.Subtration \n 3.Multiplication \n 4.Division \n 5.Modulas \n --> " ))

if operation==1:
    result = num1 + num2

elif operation==2:
    result = num1 - num2


elif operation==3:
    result = num1 * num2


elif operation==4:
    result = num1 / num2

elif operation==5:
    result = num1 % num2

else:
    print("Invalid operation")

print("Answer = ",result)

    