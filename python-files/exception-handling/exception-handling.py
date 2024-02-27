###################### EXCEPTION HANDLING ################################

try:
    x = int(input("enter first no: "))
    y = int(input("enter second no: "))

    print(x/y)
    print("Thanks for using our program")

except ZeroDivisionError:
    print("Sorry you provided a zero, which is not allowed")


try:
    arr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(arr_list[9])

except IndexError as err:
    print("that index is not found", err)


# used when I don't know the particaular error to expect

try:
    arr_list = [1, 2, 3, 4, 5, 6, 7]
    print(arr_list[7])

except Exception as err:
    print(" index not found", err)
