import os
import shutil
from colorama import init, Fore

# Global variable to store the paths of moved files for undo functionality
moved_files_history = []

def welcome_note():
    print("Welcome to the File Organizer!")
    print("This program helps you organize files in a folder by moving files with specified extensions or filenames to a destination folder.")
    print("Follow the instructions to get started.\n")

def move_files_to_destination(fold_path, fil_exts, dest_folder):
    try:
        global moved_files_history
        moved_files_history = []  # Clear the moved files history for each operation

        # Check if the provided folder path exists
        if not os.path.exists(fold_path):
            print(Fore.RED + "✘ Error: Folder path does not exist")
            return
        
        # List files in the provided directory path
        files = os.listdir(fold_path)
        print(Fore.GREEN + "\n✔ Files in directory:")
        # Iterate over files and print each file name on a new line
        for file in files:
            print(file)

        # Create destination folder path
        dest_path = os.path.join(fold_path, dest_folder)

        # Check if the destination folder already exists. If not, create it.
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            print(Fore.GREEN + f"\n✔ Destination folder '{dest_folder}' created.")

        # Move files with the specified extensions/filenames to the destination folder
        moved_files = 0
        for file in files:
            f_name, f_exten = os.path.splitext(file)
            # Check if the file extension or filename matches any of the provided extensions/filenames
            if f_exten[1:].lower() in fil_exts or f_name.lower() in fil_exts:
                src_file = os.path.join(fold_path, file)
                dest_file_name = file
                # Check if the destination folder already contains a file with the same name
                while os.path.exists(os.path.join(dest_path, dest_file_name)):
                    # Append "copy" to the file name
                    dest_file_name = f_name + "_copy" + f_exten
                dest_file = os.path.join(dest_path, dest_file_name)
                shutil.move(src_file, dest_file)
                moved_files += 1
                moved_files_history.append((dest_file, src_file))  # Store the moved file paths for undo

        print(Fore.GREEN + f"\n✔ {moved_files} file(s) have been moved to '{dest_folder}' folder.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(Fore.RED + f"✘ Error: {e}")

def undo_last_operation():
    global moved_files_history
    if moved_files_history:
        for dest_file, src_file in moved_files_history:
            shutil.move(dest_file, src_file)
        print(Fore.GREEN + "\n✔ Last operation undone successfully.")
        moved_files_history = []  # Clear the moved files history after undo
    else:
        print(Fore.YELLOW + "\n⚠ There are no operations to undo.")

def main():
    init(autoreset=True) # Initialize colorama

    welcome_note()

    try:
        # Get folder path from the user
        fold_path = input("Enter the folder path where the files are located: ")

        # Get the file extensions or filenames from the user (comma-separated)
        fil_ext_input = input("Enter the file extensions or filenames (comma-separated): ")
        fil_exts = [ext.strip().lower() for ext in fil_ext_input.split(",")]

        # Ask the user to enter the destination folder name
        dest_folder = input("Enter the destination folder name: ")

        move_files_to_destination(fold_path, fil_exts, dest_folder)

        # Confirmation prompt
        confirm = input("\nDo you want to proceed with the operation? (yes/no): ").lower()
        if confirm == "yes":
            print("\nOperation confirmed. Files organized successfully!")
        else:
            undo_last_operation()  # Undo the operation if not confirmed
            print("\nOperation cancelled by user.")
        
        print("\nThanks for using file organizer! 👍👍👍")
        print("\nCreated by CletsyMedia! 👍👍👍")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user 😪😪😪.")
    except Exception as e:
        print(Fore.RED + f"✘ Error: {e}")

if __name__ == "__main__":
    main()
