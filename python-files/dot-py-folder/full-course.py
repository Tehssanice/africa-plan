# !/usr/bin/python3
# # PYTHON SYLLABLES
# import random


# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # INTO TO PYTHON


# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # LISTS


# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # IF STATEMENTS


# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # DICTIONARIES
################### Example code  ##################################

def kill_alien():
    alien = {'color': 'green', 'points': 5}
    user_input = input("Did you shoot down an alien?")

    if user_input == "yes":
        new_points = alien['points'] + 1
        alien['color'] = "blue"
        color = alien['color']
        print(
            f"You just earned {new_points} points and the color has chaged to {color} !")

    elif user_input == "no":
        new_points = alien['points'] - 1
        color = alien['color'] = "red"
        print(
            f"Your point has been reduced to {new_points} and the color has chaged to {color}  ")

    else:
        print(f"Game over")


# kill_alien()

################### Modifying Values in a Dictionary   #############################


def modify_dict():
    alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
    print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
    if alien_0['speed'] == 'slow':

        x_increment = -1

    elif alien_0['speed'] == 'medium':

        x_increment = 0

    else:
        x_increment = 2

# # The new position is the old position plus the increment.
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print(f"New position: {alien_0['x_position']}")


###################### Removing Key-Value Pairs  ###########################
    alien_dict = {'color': 'red', 'points': 12}
    print(alien_dict)
    del alien_dict['points']
    print(alien_dict)


# modify_dict()

################### A Dictionary of Similar Objects    #############################

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


def dict_of_similar_obj():

    language = favorite_languages['sarah'].title()
    print(f"Sarah's favorite language is {language}.")


# For dictionaries, specifically, you can use the get() method to set a default value that will be returned if the requested key doesn’t exist.
# The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist:

    alien_0 = {'color': 'green'}
    point_value = alien_0.get('points', 'No point value assigned.')
    print(point_value)


# dict_of_similar_obj()


###################  CREATING A GLOSSARY   ##############################

def glossary_dict():
    glossary = {
        'Bug': ' \n Programmers use the phrase bug to refer to broken code with a fault or flaw.',
        'Build': ' \n  Build is the stage of software development in which you create the product.',
        'Back-end': ' \n  Back end is the server side of the internet or an application.',
        'Cloud': ' \n  The cloud is a remote internet storage solution.'
    }

    glossary['Algorithm'] = "An algorithm is a set of instructions that are followed to solve a problem. It's a computer's thought process."
    glossary['Arrays'] = "Arrays are containers that hold variables; they're used to group together similar variables. "
    glossary['Bit'] = "The individual 1's and 0's you see in binary are called bits. "
    glossary['Coding'] = "Coding is how people create instructions for computers to follow. "

    for key, value in glossary.items():
        print(f"\n {key}:")
        print(f" {value}")


# glossary_dict()


rivers = {
    'nile': 'Egypt',
    'chari river': 'Chad',
    'congo river': 'Congo'
}


def river_dict():

    for key, value in rivers.items():
        print(f"{key.title()} runs in {value}")


# river_dict()

############## LOOPING Through All Key-Value Pairs using items() method  ########################


def loop_using_items():
    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
    }

    for key, value in user_0.items():

        print(f"\nKey: {key}")
        print(f"Value: {value}")

    for name, language in favorite_languages.items():

        print(f"{name.title()}'s favorite language is {language.title()}.")


# loop_using_items()

############# LOOPING Through All Key-Value Pairs using keys() method  #####################


def loop_using_keys():

    friends = ['jen', 'phil', 'edward']

    for name in favorite_languages.keys():
        print(name.title())
    if name in friends:

        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

    for key in rivers.keys():
        print(f"{key}")

    name_for_poll = ['sarah', 'jane', 'edward', 'lamb', 'sam']

    for name in name_for_poll:
        if name in favorite_languages:
            print(f"{name} thank you for your participation")
        if name not in favorite_languages:
            print(f"{name} kindly take the poll")


############## Looping Through a Dictionary’s Keys in a Particular Order. sorted() helps to to arrange items in alphabetical order  #########################
    for name in sorted(favorite_languages.keys()):
        print(f"{name.title()}, thank you for taking the poll.")


# loop_using_keys()


############## LOOPING Through All Values in a Dictionary  ##################################
def loop_using_values():

    for language in favorite_languages.values():
        print(f"{language.title()}")

    for country in rivers.values():
        print(f"{country}")


# A set is a collection in which each item must be unique:
    print("The following languages have been mentioned:")
    for language in set(favorite_languages.values()):
        print(language.title())


# loop_using_values()


####################### NESTING DICTIONARIES ###############################

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}


def nesting_dict():

    aliens = [alien_0, alien_1, alien_2]

    for alien in aliens:
        print(alien)

    # Make an empty list for storing aliens.
    aliens = []

# Make 30 green aliens.
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 7, 'speed': 'fast'}
        aliens.append(new_alien)

# Show the first 5 aliens.
    for alien in aliens[:5]:
        print(alien)
    print("...")
# Show how many aliens have been created.
    print(f"Total number of aliens: {len(aliens)}")

    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10

        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15

    print(f"3 aliens updated {alien}")


# nesting_dict()


########################### A List in a Dictionary   ##############################
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}


def list_in_dict():
    # Summarize the order.
    print(f"You ordered a {pizza['crust']}-crust pizza "
          "with the following toppings:")
    for topping in pizza['toppings']:
        print("\t" + topping)

    favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
    }

    for name, languages in favorite_languages.items():
        print(f"\n{name.title()}'s favorite languages are:")

        for language in languages:
            print(f"\t{language.title()}")


# list_in_dict()

################### A Dictionary in a Dictionary  ############################

def dict_in_dict():
    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
        },
    }

    for username, user_info in users.items():

        print(f"\nUsername: {username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']
        print(f"\tFull name: {full_name.title()}")
        print(f"\tLocation: {location.title()}")


# dict_in_dict()


# Example inventories
inventory1 = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 12
}

inventory2 = {
    "apple": 15,
    "banana": 7,
    "grape": 10,
    "watermelon": 3
}


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
