# 1. Write a Python program that divides two numbers entered by the user. Handle the
# ZeroDivisionError excepton if the user tries to divide by zero.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    dividend = num1 / num2

except ZeroDivisionError:
    print("You encountered an error due to division by zero")


# 2. Create a function that takes two integers as input and returns their division. Handle
# the ZeroDivisionError exception within the function.

import sys


def division():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        dividend = num1 / num2

        return dividend

    except ZeroDivisionError:
        print("Division by zero caused an error")


division()

# 3. Write a program that asks the user to input their age. Handle the ValueError
# exception if the user enters something other than an integer.

try:
    user_age = int(input("Enter your age: "))

    print(f"User age is {user_age}")

except ValueError:
    print(f"Age is not a a valid input")


# 4. Create a function that takes a list of numbers as input and returns the average of
# those numbers. Handle the TypeError exception if the input is not a list.

def average_of_numbers():
    try:
        number_input = input("Enter numbers separated by commas: ")

        num_list = [int(num) for num in number_input.split(",")]

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


average_of_numbers()


# 5. Write a program that opens a file specified by the user. Handle the
# FileNotFoundError exception if the file does not exist.

try:
    file = open('error-file.txt', 'r')

except FileNotFoundError as e:
    print(f"File does not exist {e}")


# 6. Create a function that takes a string as input and converts it to an integer. Handle the
# ValueError exception if the string cannot be converted to an integer.

def string_to_int():
    try:
        str_input = int(input("Enter a string: "))

        print(str_input)

    except ValueError as err:
        print(f"Input is not a valid string {err}")


string_to_int()

# 7. Write a program that asks the user to input a number. Handle the KeyboardInterrupt
# exception if the user interrupts the program.

try:
    num_input = int(input("Enter a number: "))
    print(num_input)

except KeyboardInterrupt:
    print(f" An interruption occcurred")


# 8. Create a function that takes a dictionary as input and prints the keys and values.
# Handle the TypeError exception if the input is not a dictionary.


# user_info = ['name', '8', 3]
user_info = {
    'name': 'Xane',
    'age': 30
}


def dict_input(user_info):

    try:

        if type(user_info) != dict:
            raise TypeError("This is not a dictionary")

        for key, value in user_info.items():
            print(key, value)

    except TypeError as e:
        print(f"{e}")


dict_input(user_info)

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


list_of_str()


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


key_error()


# 11. Create a function that takes two integers as input and raises one to the power of the
# other. Handle the OverflowError exception if the result is too large to be represented.


def raise_to_power(main_num, exponential_num):
    try:
        output = main_num ** exponential_num

        if output > 1000000:
            raise OverflowError("Result is too large to be represented")
        print(output)

    except OverflowError as err:
        print(f"Error: {err}.")


raise_to_power(12, 6)


# 12. Create a function that takes a list of numbers as input and returns the product of
# those numbers. Handle the IndexError exception if the list is empty.

def product_of_num():
    try:
        numbers = [2, 16]
        product = 1

        if numbers == []:
            raise IndexError("List is empty")

        if type(numbers) != list:
            print("Input is not a list")
            return None

        for i, num in enumerate(numbers):

            if type(numbers[i]) != int:
                print("Input contains a invalid value")
                return None

            product *= num
            print(product)

    except IndexError as e:
        print(f"{e}")


product_of_num()


# 13. Write a program that prompts the user to enter a valid email address. Handle the
# AssertionError exception if the email address does not contain an "@" symbol.

def email_verification(email):
    try:
        email = input("Enter your email: ")

        if '@' in email:
            print("Email verified")
        else:
            raise AssertionError("Add a valid email, yours is missing @")

    except AssertionError as E:
        print(f"{E}")


email_verification()

# 14. Create a function that takes a list of integers as input and returns the sum of the
# squares of those integers. Handle the ValueError exception if any element in the list
# cannot be squared.


def sum_of_squares(int_list):
    try:
        int_list = [2, 4, '7', 55]
        total = 0

        for num in int_list:
            if type(num) == str:
                raise ValueError("Input contains an invalid value")

            else:
                square = num ** 2
                total += square
                print(total)

    except ValueError as e:
        print(f"{e}")


sum_of_squares()

# 15. Write a program that reads an integer from the user and prints its factorial. Handle
# the RecursionError exception if the factorial function exceeds the maximum
# recursion depth.


def factorial(number):
    try:
        result = 1
        limit = sys.getrecursionlimit()

        for i in range(1, number + 1):
            result *= i
            if result > limit:
                raise RecursionError("Max recursion limit reached")

        print(result)

    except RecursionError as err:
        print(f"Error: {err}")


factorial(9)


# 16. Create a function that takes a string as input and converts it to uppercase. Handle the
# ATributeError exception if the input is not a string.

def uppercase(string):
    try:
        new_string = string.upper()
        print(new_string)

    except AttributeError:
        print("Input is not a string")


uppercase(6)


# 17. Write a program that asks the user to input a list of numbers separated by commas.
# Convert the input string to a list of integers and handle the ValueError exception if
# any element cannot be converted.

def str_to_int():
    try:
        num_list = ['1', 'r', '3', 'u', '5', '6']

        new_num_list = [int(num) for num in num_list]
        print(new_num_list)

    except ValueError:
        print("Value cannot be coverted")


str_to_int()

# 18. Create a function that takes two strings as input and concatenates them. Handle the
# TypeError exception if either input is not a string.


def concatenation():
    try:

        string1 = 'jump'
        string2 = 4

        full_string = string1 + string2

        for string in full_string:
            if type(string) != str:
                raise TypeError()

        print(full_string)

    except TypeError as e:
        print(f"{e}")


concatenation()

# 19. Write a function that takes two numbers as input and performs various arithmetic
# operations (addition, subtraction, multiplication, division). Handle both
# ZeroDivisionError and TypeError exceptions if they occur.


def arithmetic_operation():
    try:

        x = 'y'
        y = 9

        sum = x + y
        multiply = x * y
        subtract = x - y
        division = x / y

        print(sum, multiply, subtract, division)
        return sum, multiply, subtract, division

    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)


arithmetic_operation()

# 20. Create a program that prompts the user to enter two integers and a mathematical
# operation (addition, subtraction, multiplication, division). Perform the operation and
# handle appropriate exceptions. Use a finally block to display a message indicating the
# end of the program.


def mathematics():
    try:

        input1 = int(input("Enter first integer: "))
        input2 = int(input("Enter second integer: "))

        sum = input1 + input2
        multiply = input1 * input2
        subtract = input1 - input2
        division = input1 / input2

        print(sum, multiply, subtract, division)
        return sum, multiply, subtract, division

    except TypeError as e:
        print(e)

    except ValueError as e:
        print(e)

    except ZeroDivisionError as e:
        print(e)

    finally:
        print("The program has ended")


mathematics()

# 21. Write a function that takes a list and an index as input and returns the element at
# that index. Handle both IndexError and TypeError exceptions that might occur.

a_list = [2, 3, 4, 5, 7, 'y', 23]


def list_and_index(a_list):
    try:

        for num in a_list:
            print(num, a_list.index(num))

    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)


list_and_index(a_list)


# 22. Create a program that asks the user to enter their name and age. Handle both
# ValueError and TypeError exceptions that might occur during the input process. Use a
# finally block to print a farewell message.

def personal_info():
    try:
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        if type(name) != str:
            raise ValueError("Please enter a string")

        if type(age) != int:
            raise TypeError("Please enter an integer")

    except ValueError as e:
        print(f"Index error: {e}")
    except TypeError as e:
        print(f"Error type: {e}")
    finally:
        print("The program has ended")


personal_info()

# 23. Write a function that takes a string as input and tries to convert it to an integer, then
# to a float. Handle both ValueError and TypeError exceptions that might occur during
# conversion.


def str_conversion():
    try:
        string_input = {'3'}

        int_value = int(string_input)
        float_value = float(int_value)

        print(int_value)
        print(float_value)

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


str_conversion()


# 24. Create a program that asks the user to input two numbers and a power exponent.
# Calculate the result of raising the first number to the power of the second number.
# Handle appropriate exceptions for invalid inputs such as non-numeric values or non-
# integer exponents. Use a finally block to display the result or an error message.


def power_exponent():
    try:
        main_num = float(input("Enter first number: "))
        exponential_number = float(input("Enter second: "))

        result = main_num ** exponential_number

        print(result)

    except ValueError as e:
        print(f"Error:{e}")
    except TypeError as e:
        print(e)


power_exponent()

# 25. Write a function that takes a list of tuples, where each tuple consists of two integers,
# and calculates the ratio of the first integer to the second integer for each tuple.
# Handle both ZeroDivisionError and TypeError exceptions that might occur during
# calculation.

tuple_list = [(10, 2), (6, 3), (6, 'k')]


def tuple_ratio(tuple_list):
    result_ratios = []

    for tuple in tuple_list:
        try:
            numerator, denominator = tuple

            if denominator == 0:
                raise ZeroDivisionError("Value indivisible by zero")

            ratio = numerator / denominator
            result_ratios.append(ratio)

        except TypeError as e:
            print(f"Error:{e} ")
        except ZeroDivisionError as err:
            print(err)

    print(result_ratios)


tuple_ratio(tuple_list)


# 26. Create a program that reads a list of integers from the user, performs a specified
# operation (e.g., sum, product), and prints the result. Handle both ValueError and
# TypeError exceptions that might occur during input or calculation. Use a finally block
# to display a message indicating the end of the program.


def read_integers():
    try:
        user_input = input("Enter a list of integers separated by commas: ")
        user_numbers = [int(num) for num in user_input.split(',')]

        operation_type = input(
            "Enter operation ('sum' or 'product'): ").lower()

        if not user_numbers:
            print("Enter an integer")
            return

        if operation_type == 'sum':
            result = sum(user_numbers)

        elif operation_type == 'product':
            result = 1

            for num in user_numbers:
                result *= num
        else:
            print("Please perform an operation, 'sum' or 'product'.")
            return

        print(f"The result of {operation_type} is: {result}")

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("The program has ended.")


read_integers()


# 27. Write a function that takes a dictionary and two keys as input and swaps the values
# associated with those keys. Handle KeyError exceptions that might occur if the keys
# are not present in the dictionary.

sample_dict = {'a': 8, 'b': 20, 'c': 9}


def swap_function(dictionary, key1, key2):
    try:

        if key1 not in dictionary:
            if key2 not in dictionary:
                raise KeyError("Key is not in dictionary")

        result_dict = dictionary[key1], dictionary[key2] = dictionary[key2], dictionary[key1]

        if result_dict:
            print("Updated Dictionary:", result_dict)
        print(f"Swap successful.")

        return dictionary

    except KeyError as ke_error:
        print(f"Error: {ke_error}")
        return None


swap_function(sample_dict, 'a', 'c')


# 28. Create a program that simulates a banking transaction. Ask the user for the amount
# to deposit and withdraw, and handle both ValueError and TypeError exceptions that
# might occur during input. Use a finally block to display the updated account balance
# or an error message.

initial_balance = 14600.0


def bank_transfer(balance):
    try:
        deposit_amount = float(input("Deposit an amount: "))
        withdraw_amount = float(input("Enter an amount to withdraw: "))

        balance += deposit_amount
        balance -= withdraw_amount

        print(f"{balance}")

    except ValueError:
        print("Enter a valid amount.")
    except TypeError:
        print("Value is invalid")
    finally:
        print("End of program.")


bank_transfer(initial_balance)
