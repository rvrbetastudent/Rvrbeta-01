"""
===========================================================
Program Name: My Python Program
Author: Your Name
Date: YYYY-MM-DD
Description:
    This program performs [brief description of functionality].
    It is designed to [specific purpose or goal].
    
Usage:
    Run the script using Python 3.x. Ensure all dependencies
    are installed before execution.

===========================================================
"""
import os
import shutil

def renumber_files(folder_path, prefix):
    """
    Renumbers files with the given prefix in the specified folder.
    
    Args:
        folder_path (str): The path to the folder containing the files.
        prefix (str): The prefix of the files to be renumbered.
    """
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if f.startswith(prefix)]
    
    # Sort the files by the numeric part of the filename
    files.sort(key=lambda x: int(x[len(prefix):].split('.')))
    
    # Renumber the files
    for i, file in enumerate(files, start=1):
        old_path = os.path.join(folder_path, file)
        new_filename = f"{prefix}{str(i).zfill(3)}.txt"
        new_path = os.path.join(folder_path, new_filename)
        shutil.move(old_path, new_path)
        print(f"Renamed {file} to {new_filename}")

# Example usage
renumber_files("path/to/folder", "spam")