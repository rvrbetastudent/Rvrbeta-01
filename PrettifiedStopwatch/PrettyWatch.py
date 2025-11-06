"""

Program Name: prettified_stopwatch.py
Author: Ryan Vrbeta
Date: 2025-11-06
Description:
This program is a command-line stopwatch utility.
It tracks total elapsed time and individual lap times.
It is designed to format the output cleanly using
string justification and to automatically copy the final
lap report to the system clipboard.

Usage:
Run the script from the command line using Python 3.x.
- Press ENTER to begin the stopwatch.
- Press ENTER again to record each new lap.
- Press Ctrl-C to stop the program.
Upon stopping, all recorded laps will be copied to the
clipboard.

Ensure the 'pyperclip' dependency is installed:
pip install pyperclip


===========================================================
"""
import time
import pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch')
print('and mark a new lap. Press Ctrl-C to quit.')

input() # Press Enter to begin.
print('Started.')
print('Laps will be copied to clipboard upon exit (Ctrl-C).')

start_time = time.time() # Get the first lap's start time.
last_time = start_time
lap_number = 1
lap_data = [] # List to store all lap strings for the clipboard.

try:
    while True:
        input()
        
        # Capture the current time once for consistent calculations
        current_time = time.time()
        
        # Calculate lap time and total time
        lap_time = round(current_time - last_time, 2)
        total_time = round(current_time - start_time, 2)
        
        # Format the output string
        # str.rjust(width) will right-justify the string within a field of 'width'
        lap_num_str = str(lap_number).rjust(2)
        total_time_str = str(total_time).rjust(6)
        lap_time_str = str(lap_time).rjust(6)
        
        output_string = f'Lap #{lap_num_str}: {total_time_str} ({lap_time_str})'
        
        print(output_string, end='')
        
        # Store the formatted string for the clipboard
        lap_data.append(output_string)
        
        lap_number += 1
        last_time = current_time # Reset the last lap time

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    
    # Join all the lap strings with a newline and copy to clipboard
    try:
        clipboard_text = '\n'.join(lap_data)
        pyperclip.copy(clipboard_text)
        print('All lap data has been copied to the clipboard.')
    except pyperclip.PyperclipException:
        print('Could not copy to clipboard. Is the pyperclip module installed correctly?')
        print('On Linux, you may need to install xclip or xsel.')