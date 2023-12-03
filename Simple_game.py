while True:
    try:
        user_input = int(input("Enter your number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # Continue to the next iteration of the loop

    choice = input("Enter 'all' for all numbers, 'odd' for odd numbers, 'even' for even numbers, or 'exit' to end: ")

    if choice == 'exit':
        print('Thank you!👍')
        break  # Exit the loop if the user enters 'exit'

    if choice == 'all':
        num = []
        number = 1
        while number <= user_input:
            num.append(number)
            number += 1
        sum_of_numbers = sum(num)
        print(f"The numbers between 1 and {user_input} are: \n {num}")
        print(f"The sum of the numbers is: \n {sum_of_numbers}")

    elif choice == 'odd':
        num = []
        number = 1
        while number <= user_input:
            num.append(number)
            number += 2
        sum_of_numbers = sum(num)
        print(f"The number inputed: {user_input}, has the following odd numbers: \n {num}")
        print(f"The sum of the odd numbers is: \n {sum_of_numbers}")

    elif choice == 'even':
        num = []
        number = 2
        while number <= user_input:
            num.append(number)
            number += 2
        sum_of_numbers = sum(num)
        print(f"The number inputed: {user_input}, has the following even numbers: \n {num}")
        print(f"The sum of the even numbers is: \n {sum_of_numbers}")

    else:
        print("Invalid choice. Please enter 'all', 'odd', 'even', or 'exit'.")
