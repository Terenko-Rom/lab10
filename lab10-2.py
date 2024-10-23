import os
import shutil as s
new_dir = 'my_pythonfile'
os.makedirs(new_dir, exist_ok=True)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files_to_copy = files[:3]
for file in files_to_copy:
    s.copy(file, new_dir)
    print(f"Скопійовано файли: {files_to_copy} у каталог {new_dir}")