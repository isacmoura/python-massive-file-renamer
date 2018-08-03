import os
import string

def rename_files():
    # receive the path of the photo from the user
    path = raw_input('Insert the path of the directory of the photos\n');
    list_photos = os.listdir(path);
    
    # Saving the current directory
    saved_path = os.getcwd();
    # changing the working directory to the local of the photos
    os.chdir(path);
    
    # for each photo in list_photos, rename them
    for file_name in list_photos:
        # if the current string isn't a string that contains numbers, so don't enter
        # the loop
        if (file_name not in file_name.translate(None, '1234567890')):
           print("Old name - " + file_name);
           print("New name - " + file_name.translate(None, '1234567890'));
           os.rename(file_name, string.translate(file_name, None, '1234567890'));
    #returning to previous directory
    os.chdir(saved_path);
rename_files();




