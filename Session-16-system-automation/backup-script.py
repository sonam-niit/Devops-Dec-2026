import os
import shutil
from datetime import datetime

source_dir='/mnt/e/Sonam-Soni/materials'
backup_dir='/mnt/e/Sonam-Soni'

# create if backup dir not exist
os.makedirs(backup_dir,exist_ok=True)

timestamp=datetime.now().strftime("%d-%m-%y_%H-%M-%S")
# backup file name
backup_file_name=f"backup-{timestamp}"
back_path=os.path.join(backup_dir,backup_file_name)

shutil.make_archive(back_path,'zip',source_dir)
print("Backup COmpleted Successfully")