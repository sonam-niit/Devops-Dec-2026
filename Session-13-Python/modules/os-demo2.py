# way 2 to import functions directly
from os import getcwd, mkdir,listdir, rename, getenv, path
cwd=getcwd() # use direct function no need to write os.
print(f"Current Working Directory: {cwd}")
print(f"List Dir: {listdir()}")

# Create new Dir
new_dir = "demo_folder"
if not path.exists(new_dir):
    mkdir(new_dir)
    print(f"Created Directory: {new_dir}")
    
# Rename Directory
rename_dir="rename_folder"
if not path.exists(rename_dir):
    rename(new_dir,rename_dir)
    print(f"Rename {new_dir} to {rename_dir}")

# Write Logic to Remove Directory
# Home Dir
print(f"Home Dir: {getenv("HOME")}")