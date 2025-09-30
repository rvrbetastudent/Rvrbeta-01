"""
===========================================================
Program Name: RenumberingFiles.py
Author: Ryan Vrbeta
Date: 1995-08-07 (Updated 2025-09-29)
Description:
    This program performs management of sequentially numbered files by either closing 
    gaps in the numbering or creating new ones.

Usage (from the command line):
    To close gaps:
        python RenumberingFiles.py close <folder_path> <prefix>
        Example: python RenumberingFiles.py close . spam

    To insert a gap:
        python RenumberingFiles.py insert <folder_path> <prefix> <position>
        Example: python RenumberingFiles.py insert . spam 42
===========================================================
"""
# --- IMPORT LIBRARIES ---
# The 'os' library lets us interact with the operating system, like listing files in a directory.
import os
# The 'shutil' library gives us tools for file operations, like renaming/moving files.
import shutil
# The 're' library is for "regular expressions," a powerful way to find patterns in text. We'll use it to find the numbers in filenames.
import re
# The 'sys' library lets us access system-specific parameters, like the arguments passed in from the command line.
import sys

def get_file_list(folder_path, prefix):
    """Scans a folder and returns a sorted list of matching numbered files."""
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found at '{folder_path}'")
        return None, 0

    # This pattern finds files that start with the prefix, followed by digits.
    # ^ asserts position at start of the string.
    # re.escape(prefix) handles special characters in the prefix.
    # (\d+) captures one or more digits (the number).
    # (.*) captures the rest of the filename (the extension).
    pattern = re.compile(rf'^{re.escape(prefix)}(\d+)(.*)')
    
    files_to_process = []
    for filename in os.listdir(folder_path):
        match = pattern.match(filename)
        if match:
            # Extract the parts of the filename
            number_str = match.group(1)
            number_int = int(number_str)
            suffix = match.group(2)
            # Store the info, including the original number string for padding reference
            files_to_process.append((number_int, number_str, suffix, filename))

    # Sort the list based on the integer value of the number
    files_to_process.sort()

    # Determine the padding width (e.g., 3 for '001') from the last file in the sequence.
    # This makes the script flexible for any amount of zero-padding.
    padding_width = len(files_to_process[-1][1]) if files_to_process else 3

    return files_to_process, padding_width

def close_gaps(folder_path, prefix):
    """Finds and closes all gaps in a numbered file sequence."""
    print(f"--- Closing gaps for prefix '{prefix}' in folder '{folder_path}' ---")
    
    files_to_process, padding_width = get_file_list(folder_path, prefix)

    if files_to_process is None: # Error already printed by get_file_list
        return
    if not files_to_process:
        print("No matching files found to process.")
        return

    expected_num = 1
    gaps_found = 0
    # Loop through the sorted list of files
    for number_int, _, suffix, original_filename in files_to_process:
        if number_int != expected_num:
            gaps_found = 1
            new_filename = f"{prefix}{str(expected_num).zfill(padding_width)}{suffix}"
            source = os.path.join(folder_path, original_filename)
            destination = os.path.join(folder_path, new_filename)

            if not os.path.exists(source):
                print(f"Source file does not exist: {source}")
                continue

            if os.path.exists(destination):
                print(f"Destination file already exists: {destination}. Skipping to avoid overwrite.")
                continue

            print(f"Renaming '{original_filename}' -> '{new_filename}'")
            shutil.move(source, destination)

        expected_num += 1

    if not gaps_found:
        print("No gaps were found.")
    else:
        print("--- Finished closing gaps. ---")

def insert_gap(folder_path, prefix, position):
    """Creates a gap in a numbered file sequence by renumbering files."""
    print(f"--- Inserting gap for prefix '{prefix}' at position {position} in folder '{folder_path}' ---")

    files_to_process, padding_width = get_file_list(folder_path, prefix)
    
    if files_to_process is None: # Error already printed
        return
    
    # Filter for files at or after the position where the gap is to be inserted
    files_to_rename = [f for f in files_to_process if f[0] >= position]

    if not files_to_rename:
        print(f"No files found at or after position {position}. A gap is already available.")
        return

    # Iterate backwards to avoid overwriting files we still need to move
    for number_int, _, suffix, original_filename in reversed(files_to_rename):
        new_number = number_int + 1
        new_filename = f"{prefix}{str(new_number).zfill(padding_width)}{suffix}"
        source = os.path.join(folder_path, original_filename)
        destination = os.path.join(folder_path, new_filename)

        if not os.path.exists(source):
            print(f"Source file does not exist: {source}")
            continue

        if os.path.exists(destination):
            print(f"Destination file already exists: {destination}. Skipping to avoid overwrite.")
            continue

        print(f"Renaming '{original_filename}' -> '{new_filename}'")
        shutil.move(source, destination)

    print(f"--- Finished inserting gap. Position {position} is now open. ---")

def main():
    """Parses command-line arguments and calls the appropriate function."""
    args = sys.argv
    
    # Check for the correct number of arguments for the 'close' command
    if len(args) == 4 and args[1].lower() == 'close':
        folder, prefix = args[2], args[3]
        close_gaps(folder, prefix)
    
    # Check for the correct number of arguments for the 'insert' command
    elif len(args) == 5 and args[1].lower() == 'insert':
        folder, prefix, position_str = args[2], args[3], args[4]
        try:
            position = int(position_str)
            if position < 1:
                print("Error: Position must be a positive number.")
                return
            insert_gap(folder, prefix, position)
        except ValueError:
            print(f"Error: Invalid position '{position_str}'. Please provide an integer.")
    
    # If arguments don't match, print the usage instructions
    else:
        print("Invalid arguments. Please use one of the following formats:")
        print("  python RenumberingFiles.py close <folder_path> <prefix>")
        print("  python RenumberingFiles.py insert <folder_path> <prefix> <position>")

if __name__ == '__main__':
    main()
