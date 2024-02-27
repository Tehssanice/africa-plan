# 1. Write a Python program that divides two numbers entered by the user. Handle the
# ZeroDivisionError excepton if the user tries to divide by zero.

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     dividend = num1 / num2

# except ZeroDivisionError:
#     print("You encountered an error due to division by zero")


# 2. Create a function that takes two integers as input and returns their division. Handle
# the ZeroDivisionError exception within the function.

def division():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        dividend = num1 / num2

        return dividend

    except ZeroDivisionError:
        print("Division by zero caused an error")


# division()

# 3. Write a program that asks the user to input their age. Handle the ValueError
# exception if the user enters something other than an integer.

# try:
#     user_age = int(input("Enter your age: "))

#     print(f"User age is {user_age}")

# except ValueError:
#     print(f"Age is not a a valid input")


# 4. Create a function that takes a list of numbers as input and returns the average of
# those numbers. Handle the TypeError exception if the input is not a list.

def average_of_numbers():
    try:
        number_input = input("Enter numbers separated by commas: ")

        num_list = [int(num) for num in number_input.split(",")]
        # num_list = number_input
        if (type(num_list) != list):
            raise TypeError("Your input is not a list")

        if not all(isinstance(i, int) for i in num_list):
            raise ValueError("Your input contains a string error")

        if num_list:
            sum_of_numbers = sum(num_list)
            average = sum_of_numbers / len(num_list)
            print(average)
        elif len(num_list) < 1:
            raise TypeError("Your list is empty...")

        else:
            raise TypeError("Your input is not a list")

    except (ValueError, TypeError) as err:
        print(err)


# average_of_numbers()


# 5. Write a program that opens a file specified by the user. Handle the
# FileNotFoundError exception if the file does not exist.

# try:
#     file = open('error-file.txt', 'r')

# except FileNotFoundError as e:
#     print(f"File does not exist {e}")


# 6. Create a function that takes a string as input and converts it to an integer. Handle the
# ValueError exception if the string cannot be converted to an integer.

def string_to_int():
    try:
        str_input = int(input("Enter a string: "))

        print(str_input)

    except ValueError as err:
        print(f"Input is not a valid string {err}")


# string_to_int()

# 7. Write a program that asks the user to input a number. Handle the KeyboardInterrupt
# exception if the user interrupts the program.

# try:
#     num_input = int(input("Enter a number: "))
#     print(num_input)

# except KeyboardInterrupt:
#     print(f" An interruption occcurred")


# 8. Create a function that takes a dictionary as input and prints the keys and values.
# Handle the TypeError exception if the input is not a dictionary.

# user_info = {
#     'name': 'Joy',
# }


def dict_input(user_info):
    person_info = {}
    person_info['name'] = input("Input your name: ")
    person_info['age'] = input("Input your age: ")

    try:
        for key, value in user_info.items():
            print(key, value)

    except AttributeError:
        print("This is not a dictionary")


# dict_input(user_info)

# 9. Create a function that takes a list of strings as input and sorts them alphabetically.
# Handle the ATributeError exception if the input is not a list of strings.


def list_of_str():
    try:
        string_list = input("Enter strings separated by commas: ")

        words = string_list.split(',')
        words.sort()

        if words:
            print(string_list)

        numbers = ' '
        numbers.sort()

    except AttributeError:
        print("Wrong attribute used")


# list_of_str()


# 10. Write a program that asks the user to input their name and age. Handle the KeyError
# exception if the user does not provide both pieces of information.

def key_error():
    try:

        user_info = {}

        user_info['user_name'] = input(f"Input your name : ")
        user_info['user_age'] = input(f"Input your age : ")

        if user_info["user_name"] == '':
            raise KeyError("Input your name")
        if user_info["user_age"] == '':
            raise KeyError("Add your age")
        print(user_info)

    except KeyError as error:
        print(error)


# key_error()


# 11. Create a function that takes two integers as input and raises one to the power of the
# other. Handle the OverflowError exception if the result is too large to be represented.


def raise_to_power(main_num, exponent):
    try:
        result = main_num ** exponent
        print(result)
        return result

    except OverflowError as err:
        print(f"Error: {err}. The result is too large to be represented.")


raise_to_power(167, 189)


# 12. Create a function that takes a list of numbers as input and returns the product of
# those numbers. Handle the IndexError exception if the list is empty.

# 13. Write a program that prompts the user to enter a valid email address. Handle the
# AssertionError exception if the email address does not contain an "@" symbol.

# 14. Create a function that takes a list of integers as input and returns the sum of the
# squares of those integers. Handle the ValueError exception if any element in the list
# cannot be squared.

# 15. Write a program that reads an integer from the user and prints its factorial. Handle
# the RecursionError exception if the factorial function exceeds the maximum
# recursion depth.

# 16. Create a function that takes a string as input and converts it to uppercase. Handle the
# ATributeError exception if the input is not a string.

# 17. Write a program that asks the user to input a list of numbers separated by commas.
# Convert the input string to a list of integers and handle the ValueError exception if
# any element cannot be converted.

# 18. Create a function that takes two strings as input and concatenates them. Handle the
# TypeError exception if either input is not a string.

# 19. Write a function that takes two numbers as input and performs various arithmetic
# operations (addition, subtraction, multiplication, division). Handle both
# ZeroDivisionError and TypeError exceptions if they occur.

# 20. Create a program that prompts the user to enter two integers and a mathematical
# operation (addition, subtraction, multiplication, division). Perform the operation and
# handle appropriate exceptions. Use a finally block to display a message indicating the
# end of the program.

# 21. Write a function that takes a list and an index as input and returns the element at
# that index. Handle both IndexError and TypeError exceptions that might occur.

# 22. Create a program that asks the user to enter their name and age. Handle both
# ValueError and TypeError exceptions that might occur during the input process. Use a
# finally block to print a farewell message.

# 23. Write a function that takes a string as input and tries to convert it to an integer, then
# to a float. Handle both ValueError and TypeError exceptions that might occur during
# conversion.

# 24. Create a program that asks the user to input two numbers and a power exponent.
# Calculate the result of raising the first number to the power of the second number.

# Handle appropriate exceptions for invalid inputs such as non-numeric values or non-
# integer exponents. Use a finally block to display the result or an error message.

# 25. Write a function that takes a list of tuples, where each tuple consists of two integers,
# and calculates the ratio of the first integer to the second integer for each tuple.
# Handle both ZeroDivisionError and TypeError exceptions that might occur during
# calculation.

# 26. Create a program that reads a list of integers from the user, performs a specified
# operation (e.g., sum, product), and prints the result. Handle both ValueError and
# TypeError exceptions that might occur during input or calculation. Use a finally block
# to display a message indicating the end of the program.

# 27. Write a function that takes a dictionary and two keys as input and swaps the values
# associated with those keys. Handle KeyError exceptions that might occur if the keys
# are not present in the dictionary.

# 28. Create a program that simulates a banking transaction. Ask the user for the amount
# to deposit and withdraw, and handle both ValueError and TypeError exceptions that
# might occur during input. Use a finally block to display the updated account balance
# or an error message.
