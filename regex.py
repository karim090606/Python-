print('Name: Shyamili Shibu \nUSN: 1AY24AI105 \nSection: O\n ')
import os
import re

def search_txt_files(directory, pattern):
    try:
        regex = re.compile(pattern)
    except re.error as e:
        print(f"Invalid regular expression: {e}")
        return

    found = False

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, start=1):
                        if regex.search(line):
                            print(f"[{filename} | Line {line_number}] {line.strip()}")
                            found = True
            except Exception as e:
                print(f"Could not open {filename}: {e}")

    if not found:
        print("No matches found.")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing .txt files: ").strip()
    regex_pattern = input("Enter a regular expression to search for: ").strip()
    search_txt_files(folder_path, regex_pattern)
