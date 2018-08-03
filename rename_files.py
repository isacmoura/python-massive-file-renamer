import os
import string

def rename_files():
    list_photos = os.listdir("/home/isacmoura/Documentos/prank");
    
    # Saving the current directory
    saved_path = os.getcwd();
    # changing the working directory to the local of the photos
    os.chdir("/home/isacmoura/Documentos/prank");
    
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




