import os
import shutil


source_path = '/Users/tessa/Documents/work/africa-plan/python-files/'
files_in_source_path = os.listdir(source_path)

target_folders = {
    '.py': '/Users/tessa/Documents/work/africa-plan/python-files/dot-py-folder/',
    '.txt': '/Users/tessa/Documents/work/africa-plan/python-files/dot-txt-folder/',
    '.jpeg': '/Users/tessa/Documents/work/africa-plan/python-files/images/',
    '.webp': '/Users/tessa/Documents/work/africa-plan/python-files/images/'

}

for file in files_in_source_path:
    for extension, target_folder in target_folders.items():
        if file.endswith(extension):
            shutil.move(os.path.join(source_path, file),
                        os.path.join(target_folder, file))
