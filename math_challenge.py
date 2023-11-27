import math
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 == 0:
    print(f"zero divide not supported")
else:
    print(f"The sum of your numbers is: {num1 + num2}\n"
      f"The difference of the numbers is: {num1 - num2}\n"
      f"The product of the numbers is: {num1 * num2}\n"
      f"The division of the numbers is: {num1 / num2}\n"
      f"The square root of the first number is: {num1 ** 0.5}\n" 
      f"The sine of the first number is: {math.sin(num1)}\n" 
      f"The cosine of the first number is: {math.cos(num1)}\n" 
      f"The first number raised to the power of 3 is: {num1 ** 3}\n"
      f"The sine of the second number is: {math.sin(num2)}\n"
      f"The cosine of the second number is: {math.cos(num2)}\n"
      f"The second number raised to the power of 3 is: {num2 ** 3}\n"
      f"The sine of the sum of both numbers is: {math.sin(num1 + num2)}\n" 
      f"The cosine of the sum of both numbers is: {math.cos(num1 + num2)}")


