import os
import py7zr
import shutil

def extract_archive(archive_path, extract_to):
    os.makedirs(extract_to, exist_ok=True)
    print(f"Extracting {archive_path} to {extract_to}...")
    with py7zr.SevenZipFile(archive_path, mode='r') as archive:
        archive.extractall(path=extract_to)
    print(f"✅ Done extracting {archive_path}!")

    # Handle nested folder (e.g., data/processed/train/train/)
    subitems = os.listdir(extract_to)
    if len(subitems) == 1:
        inner_path = os.path.join(extract_to, subitems[0])
        if os.path.isdir(inner_path):
            for filename in os.listdir(inner_path):
                shutil.move(os.path.join(inner_path, filename), extract_to)
            os.rmdir(inner_path)
            print(f"✅ Flattened folder structure in {extract_to}")

if __name__ == "__main__":
    extract_archive("data/raw/train.7z", "data/processed/train")
    extract_archive("data/raw/test.7z", "data/processed/test")

