import os

file1 = open("example.txt", "w")
file1.write("Hey there, this is file handling.  "
            "\n Character	Meaning "
            "\n 'r'	open for reading (default)"
            "\n 'w'	open for writing, truncating the file first"
            "\n 'x'	create a new file and open it for writing "
            "\n 'a'	open for writing, appending to the end of the file if it exists "
            "\n 'b'	binary mode "
            "\n 't'	text mode (default)"
            "\n 'r+'	open a file for updating (reading and writing)")


file1 = open("example.txt", "a+")
file1.write("\n I just learnt how to update")

file1.seek(0)

print(file1.read())

file1.close()

# for w+, we write then read
# for r+, we read then write


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
