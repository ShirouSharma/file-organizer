import os
import shutil

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

def get_file_extension(filename):
    _, ext = os.path.splitext(filename)
    return ext[1:].upper() if ext else "NoExtension"

def resolve_duplicate_filename(dest_path, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(dest_path, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print("No files found in the directory.")
        return

    print(f"Found {len(files)} files to organize.")

    for filename in files:
        ext = get_file_extension(filename)
        
        if filename.startswith('.'):
            print(f"Skipping hidden file: {filename}")
            continue

        dest_folder = os.path.join(directory, ext)
        create_folder_if_not_exists(dest_folder)

        src_path = os.path.join(directory, filename)
        dest_filename = resolve_duplicate_filename(dest_folder, filename)
        dest_path = os.path.join(dest_folder, dest_filename)

        try:
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {dest_folder}")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

def main():
    directory = "./messy_folder"
    print(f"Organizing files in: {directory}")
    organize_files(directory)
    print("File organization complete!")

if __name__ == "__main__":
    main()