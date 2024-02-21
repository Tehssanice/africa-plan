friends = ["Sommie", "Glorie", "Faith", "Kosi"]

print(friends[0])
print(friends[-1])

message = f"I knew {friends[1]} first."
print(message)


message = f"I knew {friends[2]} second."
print(message)


mode_of_transport = ["Bently", "Porshe", "yacht", "Private jet"]

message = f"I would like to own a {mode_of_transport[0]}"
print(message)

# title() helps to format the item in the list to capitalize
message = f"Riding a {mode_of_transport[2].title()} would be amazing"
print(message)


# modigying element in a list 
friends[0] = "Chisom"
print(friends)

# A dding element to a list
friends.append("Wendy")
print(friends)


cars = []

cars.append("mercedes")
cars.append("toyota")
cars.append("ford")

print(cars)


#insert elements in a list

cars.insert(-2, "Buggatti")
cars.insert(3, "Jeep")
print(cars)

# deleting element from a list
del cars[2]
print(cars)

# removing last item from a list using the pop method, this allows us to use the removed item again

removed_car = cars.pop()
callItem = f"The removed car is {removed_car}"
print(callItem)

# Removing an item by value
oldest_car = "Jeep"

cars.remove(oldest_car)
print(cars)


guest_list = ["Myles", "Set", "Claire"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[1:12:2])

def create_palindrome(word):
    # Reverse the word and concatenate it with the original word
    palindrome = word + word[::-1]
    return palindrome

# Example:
original_word = ['m', 'a', 'd', 'a', 'm']
result = create_palindrome(original_word)

print(f"Original Word: {original_word}")
print(f"Palindrome: {result}")

