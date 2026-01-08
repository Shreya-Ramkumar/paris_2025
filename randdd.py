import os
from pathlib import Path

# Set the folder path
folder_path = "static/photos/photos3/"

# Get all image files (you can add more extensions as needed)
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
files = sorted([f for f in os.listdir(folder_path) 
                if os.path.splitext(f)[1].lower() in image_extensions])

# Rename files
for index, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    extension = os.path.splitext(filename)[1]
    new_path = os.path.join(folder_path, f"{index}{extension}")
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} → {index}{extension}")

print(f"Total files renamed: {len(files)}")