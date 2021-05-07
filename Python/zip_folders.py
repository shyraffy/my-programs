# Created by Shyraffy
# This script zips all the folders in the source directory and puts 
# the zip file in the destiny directory.

import shutil
import os, sys

def zip_folders(src, dest):
    # Makes a list with all the folders in the source directory
    folders = [folder for folder in os.listdir(src) if os.path.isdir(os.path.join(src, folder))]

    print('Zipping folders...\n')

    folder_count = 1

    try:
        for folder in folders:
            os.chdir(dest)
            print('Zipping {folder}...({}/{})'.format(folder_count, len(folders)))
            shutil.make_archive(folder, 'zip', os.path.join(src, folder))
            print(f'Zipped {folder} succesfully.')
            
            folder_count += 1

        print('\nAll folders zipped')

    except shutil.Error as error:
        print('An error ocurred!')
        print(error)
        
    except KeyboardInterrupt:
        print('Process interrupted')
  

if __name__ == '__main__':
    src = sys.argv[1]
    dest = sys.argv[2]

    if (os.path.isdir(src) and os.path.isdir(dest)):
        zip_folders(src, dest)
    else:
        print('\n You must spefify a directory!')
        sys.exit(1)
    
