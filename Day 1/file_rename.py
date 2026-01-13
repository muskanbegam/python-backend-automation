import os

# Path of the folder containing files
folder_path = "files"

# Get list of all items in the folder.
files = os.listdir(folder_path)

count = 1

for filename in files:
    old_path = os.path.join(folder_path, filename)

    # Skip if it's not a file
    if not os.path.isfile(old_path):
        continue

    # Split filename and extension
    name, extension = os.path.splitext(filename)

    # Create new filename
    new_name = f"yooo_{count}{extension}"
    new_path = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(old_path, new_path)

    count += 1

print("Batch rename completed successfully.")
