import os
import hashlib

#Generate MD5 hash for the file
def hash_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

#Find duplicate files in the folder comparing hashes
def find_duplicates(directory):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = hash_file(filepath)
            if file_hash in hashes:
                duplicates.append(filepath)
            else:
                hashes[file_hash] = filepath

    return duplicates
#Delete the duplicated files
def delete_files(file_list):
    for filepath in file_list:
        os.remove(filepath)
        print(f"Deleted {filepath}")

if __name__ == "__main__":
    directory = input("Please enter the directory path to search for duplicates: ")
    if os.path.isdir(directory):
        duplicates = find_duplicates(directory)
        if duplicates:
            print(f"Found {len(duplicates)} duplicate files.")
            delete_files(duplicates)
        else:
            print("No duplicate files found.")
    else:
        print("The provided path is not a valid directory.")
