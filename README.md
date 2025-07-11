# File Organizer

A Python script to organize files in a directory by their file extensions (e.g., .jpg, .pdf). Files are moved into folders named after their extensions (e.g., JPG, PDF).

# Features
- Sorts files by extension.
- Handles files without extensions.
- Avoids overwriting duplicates by appending numbers (e.g., `photo_1.jpg`).
- Skips hidden files.

# Usage
1. Run `create_test_files.py` to generate a `messy_folder` with test files.
2. Run `organize_files.py` to organize files in `messy_folder`.

```bash
python create_test_files.py
python organize_files.py