import os  
cwd=os.getcwd()
print(f"Current Working Directory: {cwd}")
print(f"List Dir: {os.listdir()}")

# Create new Dir
new_dir = "demo_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Created Directory: {new_dir}")
    
# Rename Directory
rename_dir="rename_folder"
if not os.path.exists(rename_dir):
    os.rename(new_dir,rename_dir)
    print(f"Rename {new_dir} to {rename_dir}")

# Write Logic to Remove Directory
# Home Dir
print(f"Home Dir: {os.getenv("HOME")}")