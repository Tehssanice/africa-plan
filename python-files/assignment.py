# TRY IT YOURSELF

# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

sommie = {
    'first_name': 'Sommie',
    'last_name': 'King',
    'city': 'Lagos',
    'age': '13'
}

# print(sommie['first_name'])
# print(sommie['last_name'])
# print(sommie['age'])
# print(sommie['city'])


# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

fav_numbers = {
    'sommie': '2',
    'kosi': '90',
    'koach': '8',
    'david': '7',
    'tessa': '11'
}

# for k, v in fav_numbers.items():
#     print(f"{k}'s favourite number is {v} ")


# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

glossary = {
    'Bug': ' Programmers use the phrase bug to refer to broken code with a fault or flaw.',
    'Build': ' Build is the stage of software development in which you create the product.',
    'Back-end': ' Back end is the server side of the internet or an application.',
    'Cloud': ' The cloud is a remote internet storage solution.'
}

# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# for key, v in glossary.items():
#     print(f"\n {key}: {v}")


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

def glossary_dict():
    glossary = {
        'Bug': ' Programmers use the phrase bug to refer to broken code with a fault or flaw.',
        'Build': ' Build is the stage of software development in which you create the product.',
        'Back-end': ' Back end is the server side of the internet or an application.',
        'Cloud': ' The cloud is a remote internet storage solution.'
    }

    glossary['Algorithm'] = "An algorithm is a set of instructions that are followed to solve a problem. It's a computer's thought process."
    glossary['Arrays'] = "Arrays are containers that hold variables; they're used to group together similar variables. "
    glossary['Bit'] = "The individual 1's and 0's you see in binary are called bits. "
    glossary['Coding'] = "Coding is how people create instructions for computers to follow. "

    for key, value in glossary.items():
        print(f"\n {key}:")
        print(f" {value}")


# glossary_dict()


# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.


rivers = {
    'nile': 'Egypt',
    'chari river': 'Chad',
    'congo river': 'Congo'
}


# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

def river_dict():

    for key, value in rivers.items():
        print(f"{key.title()} runs in {value}")


# river_dict()


# • Use a loop to print the name of each river included in the dictionary.
# for key in rivers.keys():
#     print(f"{key}")


# # • Use a loop to print the name of each country included in the dictionary.
# for country in rivers.values():
#     print(f"{country}")


# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

polling = ['sarah', 'jane', 'edward', 'lamb', 'sam']


# • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

# for name in polling:
#     if name in favorite_languages:
#         print(f"{name} thank you for your participation")
#     if name not in favorite_languages:
#         print(f"{name} kindly take the poll")

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

sommie = {
    'first_name': 'sommie',
    'last_name': 'King',
    'city': 'Lagos',
    'age': '13'
}

liam = {
    'first_name': 'liam',
    'last_name': 'Blink',
    'city': 'Texas',
    'age': '23'
}

xane = {
    'first_name': 'xane',
    'last_name': 'Jane',
    'city': 'Ohio',
    'age': '34'
}

people = [sommie, liam, xane]

# for person in people:
#     print(f"{person['first_name'].title()}:")
#     for k, v in person.items():
#         print(f"\t{k}: {v}")


# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

dog = {
    'kind': 'mammal',
    'owner': 'klint'
}

snake = {
    'kind': 'reptile',
    'owner': 'jade'
}

cat = {
    'kind': 'mammal',
    'owner': 'ben'
}

crocodile = {
    'kind': 'reptile',
    'owner': 'sam'
}

lion = {
    'kind': 'mammal',
    'owner': 'ken'
}

pets = ['dog', 'lion', 'cat', 'snake', 'crocodile']

# for pet in pets:
#     print(f"{pet}:")
#     for animal, details in pet.items():
#         print(f"\t{animal}: {details}")


# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favourite_places = {
    'helen': ['Bagan Myanmar', 'Hallstatt Austria'],
    'cynthia': ['Lapland Finland', 'Chamarel Mauritius', 'Petra Jordan'],
    'chisom': ['Barcelona Spain']
}

# for person, places in favourite_places.items():
#     if len(places) > 1:
#         print(f"{person.title()}'s favourite places are : ")
#         for place in places:
#             print(f"\t{place}")
#     else:
#         for place in places:
#             print(f"{person.title()}'s favourite place is : {place}  ")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

fav_numbers = {

    'sommie': ['2', '4', '29'],
    'kosi': ['90', '7', '90'],
    'koach': ['8', '0'],
    'david': ['7', '22'],
    'tessa': ['11', '44']
}

# for person, numbers in fav_numbers.items():
#     print(f"{person.title()}'s favourite numbers are : ")
#     for number in numbers:
#         print(f"{number}")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.


cities = {
    'Rio de Janeiro': {
        'population': '7 million',
        'country': 'Brazil',
        'fact': 'Rio de Janeiro is an extremely popular tourist resort and the cultural capital of Brazil.'

    },

    'Sao Paulo.': {
        'population': '12 million',
        'country': 'Brazil',
        'fact': 'It is popular for nightlife, cafes and architecture '

    },

    'Lagos': {
        'population': '21 million',
        'country': 'Nigeria',
        'fact': 'Most populous city in Nigeria'

    }

}

# for city, city_details in cities.items():

# print(f"\n {city}:")
# print(f"\tPopulation: {city_details['population']}")
# print(f"\tCountry: {city_details['country']}")
# print(f"\tFact: {city_details['fact']}")


# 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.


######################## CLASSWORK ##############################
# Question 1
# Example inventories
inventory1 = {"apple": 10, "banana": 5, "orange": 8, "grape": 12}
inventory2 = {"apple": 15, "banana": 7, "grape": 10, "watermelon": 3}
# Given two dictionaries above representing the inventory of two stores, write a program to
# find the items that are common to both stores and their quantities.


def common_items():
    items = {}
    for key, value in inventory1.items():
        if key in inventory2:
            items[key] = value + inventory2[key]
    print(f"Items that are common in both inventories are {items}")


# common_items()

# Question 2
# Write a program that takes a list of dictionaries representing sales data for different products,
# where each dictionary contains the product name, quantity sold, and price. Calculate the total
# sales for each product and print a summary.

sales_data = [
    {"product": "apple", "quantity_sold": 100, "price": 0.5},
    {"product": "banana", "quantity_sold": 80, "price": 0.4},
    {"product": "orange", "quantity_sold": 120, "price": 0.6},
    {"product": "grape", "quantity_sold": 60, "price": 0.8}
]


def total_sales():

    print(f"Product Summary:")

    for sale in sales_data:
        product_name = sale["product"]
        quantity_sold = sale["quantity_sold"]
        price = sale["price"]

        print(
            f" {product_name} total sale is :  {quantity_sold * price}")

# total_sales()


# Question 3
# Implement a program that takes a dictionary of words and their frequencies and finds the top
# n most frequent words efficiently.i would provide the value of n on testing

word_freq = {
    "hello": 10,
    "world": 20,
    "python": 15,
    "programming": 5,
    "is": 30,
    "awesome": 12,
    "dictionary": 8,
    "challenge": 3,
    "openai": 7,
    "gpt": 9
}

# change the dict to a list of tuples to make the items in the dict accessible for sorting
items_in_word_freq = list(word_freq.items())

# print((items_in_word_freq[1][1]))

# save the length of the list in a variable
lib_length = ((len(items_in_word_freq)))

for index in range(lib_length):
    for next_index in range(index + 1, lib_length):
        if items_in_word_freq[index][1] < items_in_word_freq[next_index][1]:
            items_in_word_freq[index], items_in_word_freq[next_index] = items_in_word_freq[next_index], items_in_word_freq[index]

# print(" Word Frequency in Descending Order:")
# for word, freq in items_in_word_freq:
#     print(f"\t{word}: {freq}")

# Question 4
# Build a simple language translation tool using dictionaries. Design dictionaries to store mappings between words in different languages.
# Write a function that takes a sentence in one language as input and translates it into another language using the dictionary mappings. Heavily use basic python types


translator = {
    'spanish': {
        'I': 'Yo',
        'am': 'soy',
        'doing': 'haciendo',
        'amazing': 'increible'

    },
    'latin': {
        'I': 'Ego',
        'am': 'sum',
        'bold': 'audax',
        'and': 'et',
        'beautiful': 'pulchra'

    },
    'french': {
        'The': 'le',
        'sky': 'ciel',
        'is': 'est',
        'bright': 'clair',
        'today': "aujourd'hui"

    },
    'japanese': {
        'I': '私',
        'live': 'ライブ',
        'healthy': '健康',

    },
    'Igbo': {
        'life': 'Ndu',
        'is': 'di',
        'good': 'mma'

    }
}

# for language, language_details in translator.items():
#     for key, value in language_details.items():
#         sentence = " ".join(language_details.keys())
#         translated_sentence = " ".join(language_details.values())
#     print(f"{sentence} is translated: \n\t{translated_sentence} in {language}")


# Question 5a

# Develop a user authentication system for a website using dictionaries. Design a dictionary
# where the keys are usernames and the values are dictionaries containing password hashes,
# email addresses, and account statuses (e.g., active or inactive). Write functions to register
# new users, authenticate existing users, and update account information.

users = {
    'Monday': {
        'password_hash': 'password',
        'email_address': 'monday@gmail.com',
        'account status': 'active',
        'role': 'admin'

    },
    'Luke': {
        'password_hash': 'password',
        'email_address': 'luke@gmail.com',
        'account status': 'inactive',
        'role': 'user'

    },
}


# new user creation
# users.update(
#     {'clara': {
#         'password_hashes': 'password',
#         'email_address': 'clara@gmail.com',
#         'account status': 'active'
#     }
#     }
# )

# register
def register(username, password, email, role):
    if username in users:
        print(f"{username} already exists")
    else:
        users[username] = {
            'password_hash': password,
            'email_address': email,
            'role': role,
            'account status': 'active'
        }
    # print(f"{username} has been registered")


# register("jane", '1234', 'jane@gmail.com', 'user')
# print(users)

# update account info

# for username, user_info in users.items():
#     if user_info['account status'] == 'active':
#         print(f"{username} is active and up to date")
#     else:
#         account_active = user_info['account status'] = 'active'
# print(
#     f" {username} has been updated: {account_active}")


def authentication(username, password):
    if users.get(username, {}).get("password_hash") == password:
        print("authentication successful")
    else:
        print("authentication failed")


# authentication('jane', '1234')
# print(users)


# Question 5b
# • Extend the user authentication system from before to include role-based access control.
# Each user now has an additional attribute specifying their role (e.g., "admin", "user").
# Write a function that authenticates users based on their username and password. If the authentication is successful, check their role:
# • If the user is an admin, grant them full access.
# • If the user is a regular user, grant them restricted access.

def role_authentication(username, role):
    if users.get(username, {}).get('role') == role:
        print("permission granted")
    else:
        print("Permission denied")


# role_authentication('jane', 'user')


# Question 6
# Create a program that takes a dictionary representing the weather forecast for a week. Each
# key is a day of the week (e.g., "Monday", "Tuesday") and the value is the forecasted
# temperature. Check if the temperature is above 80 degrees Fahrenheit for at least three
# consecutive days. If it is, print a message indicating a heatwave warning.

weather = {
    'sunday': 32,
    'monday': 65,
    'tuesday': 40,
    'wednesday': 82,
    'thursday': 88,
    'friday': 49,
    'saturday': 90

}


def forecast():
    for key, value in weather.items():
        if value > 80:
            print("A heat wave is coming")
        else:
            print("Weather is cool")


# forecast()

# Question 7
# Create a recipe book application using dictionaries. Each recipe can have attributes such as name, ingredients, and instructions.
# Write functions to add new recipes, search for recipes by ingredient, and generate shopping lists.

recipe_book = {
    'recipe1': {
        'name': 'jollof rice',
        'ingredients': ['tomato', 'carrot', 'rice', 'water', 'salt', 'pepper'],
        'instructions': ['Boil the rice for twenty minutes', 'blend the tomato and pepper']
    }
}

# Question 8
# Build a project management tool that uses dictionaries to store project details. Each project has attributes such as name, start date, end date, and tasks.
# Implement functions to add new projects, assign tasks to team members, and track project progress.

project_manager = 
