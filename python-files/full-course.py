#!/usr/bin/python3
# PYTHON SYLLABLES
import random


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# INTO TO PYTHON


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# LISTS


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# IF STATEMENTS


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# DICTIONARIES
# Example code

def kill_alien():
    alien = {'color': 'green', 'points': 5}
    user_input = input("Did you shoot down an alien?")

    if user_input == "yes":
        new_points = alien['points'] + 1
        print(f"You just earned {new_points} points!")

    elif user_input == "no":
        new_points = alien['points'] - 1
        print(f"Your point has been reduced to {new_points} ")

    else:
        print(f"Game over")


kill_alien()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# INPUTS & LOOPS


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# FUNCTION

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# CLASSES


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# FILE MGT & ERROR HANDLING


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# CODE TESTING

# print(random.randrange(51, 69))
