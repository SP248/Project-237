import os
import shutil

def organize_files(source_directory):
    directories = {'.txt': 'Text Files', '.pdf': 'PDF Files', '.jpg': 'Image Files'}
    for extension, directory_name in directories.items():
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

    for filename in os.listdir(source_directory):
        if os.path.isfile(os.path.join(source_directory, filename)):
            extension = os.path.splitext(filename)[1].lower()
            if extension in directories:
                shutil.move(os.path.join(source_directory, filename),
                            os.path.join(directories[extension], filename))


organize_files('path/to/source/directory')