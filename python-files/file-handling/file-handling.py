import os

file = open("example.txt", "w")
file.write("Hey there, thia is file handling.  "
           "\n Character	Meaning "
           "\n 'r'	open for reading (default)"
           "\n 'w'	open for writing, truncating the file first"
           "\n 'x'	create a new file and open it for writing "
           "\n 'a'	open for writing, appending to the end of the file if it exists "
           "\n 'b'	binary mode "
           "\n 't'	text mode (default)"
           "\n '+'	open a disk file for updating (reading and writing)")
file.close()


with open("example.txt", "a") as file:
    file.write("I just made some correction")


# The code below checks for a file which does not exist and uses the FileNotFoundError to handle exceptions

try:

    with open("txt2.txt", "r") as file:
        file.write("Javascript is cool")

except FileNotFoundError:
    print("Error: File does not exist")


# Different types of libraries

# 1. os


current_working_dir = os.getcwd()
print(current_working_dir)

list_dir = os.listdir()
print(list_dir)

new_dir = os.mkdir("my_new_file")

for i in list_dir:
    i.split(".")

    if i in list_dir:
        if i.split(".")[-1] == "py":
            os.mkdir("new_doc")
