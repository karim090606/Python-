print('Name: karim s mulla \nUSN: 1AY24AI052\nSection: M\n ')
import os
import re
def close_gaps(folder, prefix, extension=".txt"):
    files = [f for f in os.listdir(folder) if f.startswith(prefix) and f.endswith(extension)]
    pattern = re.compile(rf"{re.escape(prefix)}(\d+){re.escape(extension)}")

   numbered_files = []
    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            numbered_files.append((number, filename))

    numbered_files.sort()

    for i, (actual_number, filename) in enumerate(numbered_files, start=1):
        new_name = f"{prefix}{i:03d}{extension}"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        if filename != new_name:
            print(f"Renaming {filename} → {new_name}")
            os.rename(src, dst)

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    file_prefix = input("Enter the file prefix (e.g., spam): ").strip()
    close_gaps(folder_path, file_prefix)

def insert_gap(folder, prefix, position, extension=".txt"):
    files = [f for f in os.listdir(folder) if f.startswith(prefix) and f.endswith(extension)]

    pattern = re.compile(rf"{re.escape(prefix)}(\d+){re.escape(extension)}")
    numbered_files = []

    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            numbered_files.append((number, filename))

    for number, filename in sorted(numbered_files, reverse=True):
        if number >= position:
            new_name = f"{prefix}{number + 1:03d}{extension}"
            src = os.path.join(folder, filename)
            dst = os.path.join(folder, new_name)
            print(f"Renaming {filename} → {new_name}")
            os.rename(src, dst)

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    file_prefix = input("Enter the file prefix (e.g., spam): ").strip()
    insert_pos = int(input("Enter the number position to insert a gap (e.g., 2 for spam002): ").strip())
    insert_gap(folder_path, file_prefix, insert_pos
