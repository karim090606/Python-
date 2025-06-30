print('Name: Shyamili Shibu \nUSN: 1AY24AI105 \nSection: O\n ')
import os
import shutil

def copy_files_with_extension(source_dir, dest_dir, extension):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files_copied = 0

    for foldername, subfolders, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.lower().endswith(extension.lower()):
                source_path = os.path.join(foldername, filename)
                dest_path = os.path.join(dest_dir, filename)

                base, ext = os.path.splitext(filename)
                count = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(dest_dir, f"{base}_{count}{ext}")
                    count += 1

                shutil.copy2(source_path, dest_path)
                files_copied += 1
                print(f"Copied: {source_path} → {dest_path}")

    print(f"\nDone! {files_copied} file(s) copied to '{dest_dir}'.")

if __name__ == "__main__":
    src = input("Enter the path to the source folder: ").strip()
    dst = input("Enter the path to the destination folder: ").strip()
    ext = input("Enter the file extension to search for (e.g., .pdf, .jpg): ").strip()
    
    if not ext.startswith("."):
        ext = "." + ext  

    copy_files_with_extension(src, dst, ext)
