# # Question 1: Create a list of strings and iterate over it to print the length of each string.
 
# string_list = ["apple", "Yam", "orange", "Rice", "Grape"]

# for item in string_list:
#   # print(f"The length of '{item}' is {len(item)} characters.")
  
#   item_list = f"The length of '{item}' is {len(item)} characters."
# # print(item_list) 



# # Question 2: Write a program to remove a specific item from the dictionary.

# # Sample dictionary
# list_items = {'name': 'Daniel', 'age': 50, 'country': 'Nigeria', 'gender': 'Male'}


# # Specify the item to be removed
# item_to_remove = 'name'

# # Check if the key exists before removing it
# if item_to_remove in list_items:
#     # Remove the specified item from the dictionary
#     del list_items[item_to_remove]
#     # print(f" Item removed from the dictionary is {item_to_remove} .")
#     # print(list_items)
    
# else:
#     print(f"{item_to_remove} not found in the dictionary.")
    
    
    
# #Question 3: Create a program that takes a list of words as input and returns a dictionary where the keys are the words and the values are the lengths of the word 


# def create_dictionary(list_of_words):
#     # Create an empty dictionary
#     word_dict = {}

#     # loop through the words in the list
#     for word in list_of_words:
#         # Assign the length of each word as the value for the corresponding key
#         word_dict[word] = len(word)

#     return word_dict

# # Get a list of words from the user
# word_input = input("Enter a list of words separated by commas: ")
# words = word_input.split(',')

# # Create the dictionary
# print(create_dictionary(words))


# BONUS QUESTION

def two_sum(nums, target):
    # Create a dictionary to store the indices of numbers
    num_indices = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is in the dictionary
        if complement in num_indices:
            # If found, return the indices of the two numbers
            return [num_indices[complement], i]

        # If complement is not found, add the current number and its index to the dictionary
        num_indices[num] = i

    # No solution found
    return None

# Example usage:
nums = [4, 7, 9, 15]
target = 16

result = two_sum(nums, target)
print(result)




