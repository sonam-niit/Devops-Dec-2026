import os
import sys
import shutil
import subprocess
from datetime import datetime

def backup_txt_files(source_folder):
    if not os.path.exists(source_folder):
        print("Source folder does not exist")
        sys.exit(1) 
    # if folder available let's take backup
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder=f"{source_folder}_backup_{timestamp}" #backup folder name
    os.makedirs(backup_folder) # create folder
    print(f"Backup folder created: {backup_folder}")

    # Copy only txt files
    for file in os.listdir(source_folder):
        if file.endswith(".txt"):
            src_path= os.path.join(source_folder,file)
            dest_path= os.path.join(backup_folder,file)
            shutil.copy(src_path,dest_path)
            print(f"copied: {file}")

    print("Backup Completed")
    return backup_folder

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Usage: python automation.py <folder_path_of_backup>")
        sys.exit(1)

    folder=sys.argv[1] 
    backup_folder= backup_txt_files(folder)

    print("Automation completed")