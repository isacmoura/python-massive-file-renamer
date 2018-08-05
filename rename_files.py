import os
import string

def rename_files():
    # receive the path of the photo from the user
    path = input('Insert the path of the directory of the photos\n');
    list_photos = os.listdir(path);
    # receive the characters that the user wants to remove from the files
    chars = input('What characters you want to remove?\n');
    
    # Saving the current directory
    saved_path = os.getcwd();
    # changing the working directory to the local of the photos
    os.chdir(path);
    
    # for each photo in list_photos, rename them
    for file_name in list_photos:
        # if the current string isn't a string that contains numbers, so don't enter
        # the loop
        new_name = file_name.translate(str.maketrans('', '', chars));
        if (file_name not in new_name):
           print("Old name - " + file_name);
           print("New name - " + new_name);
           os.rename(file_name, new_name);
    # returning to previous directory
    os.chdir(saved_path);
rename_files();
