import os

def create_test_files():
    folder = "./messy_folder"
    os.makedirs(folder, exist_ok=True)
    
    # List of test files to create
    test_files = [
        "photo1.jpg", "photo2.jpg", "vacation.jpg",
        "document1.pdf", "document2.pdf", "report.pdf",
        "notes.txt", "readme.txt", "todo.txt",
        "script.py", "app.py",
        "song.mp3", "podcast.mp3",
        "data.csv", "results.csv",
        "noextension",  # File without extension
        "image.png", "logo.png",
        "video.mp4",
        "archive.zip"
    ]
    
    # Create empty files
    for filename in test_files:
        with open(os.path.join(folder, filename), "w") as f:
            f.write("This is a test file.")
        print(f"Created: {filename}")

if __name__ == "__main__":
    create_test_files()