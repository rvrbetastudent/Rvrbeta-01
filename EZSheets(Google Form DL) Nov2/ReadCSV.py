"""
===========================================================
Program Name: ReadCSV.py
Author: Ryan Vrbeta
Date: 2025-10-21

Description:
    This program connects to a Google Sheets document using the EZSheets
    library and retrieves data from a linked Google Form response sheet.
    It authenticates via OAuth 2.0 credentials, reads the spreadsheet,
    and can export the data as a CSV file for offline use or analysis.
    
Usage:
    1. Ensure Python 3.x is installed.
    2. Install dependencies:
           pip install ezsheets
    3. Place your 'credentials-sheets.json' file in the same directory.
    4. Run the script:
           python ReadCSV.py
    5. On first run, a browser window will open for Google account authorization.
       Once authorized, a 'token-sheets.pickle' file will be created to save
       your login session for future use.

Dependencies:
    - ezsheets
    - Google Sheets access (OAuth credentials)

===========================================================
"""
import ezsheets

# Initialize
ezsheets.init(credentialsFile=r'C:\Users\shrek\source\repos\rvrbetastudent\Rvrbeta-01\Oct26\credentials-sheets.json')

# Open your spreadsheet
sheet_id = "1sxqyi0VzzIHNXg5MPlomxpgQF-B9NkVLZKMGJOIghD8"
spreadsheet = ezsheets.Spreadsheet(sheet_id)

# Select the Form Responses sheet
form_sheet = spreadsheet['Form Responses 1']

# Get all rows
rows = form_sheet.getRows()

# Filter out empty rows and cells
clean_rows = [ [cell for cell in row if cell] for row in rows if any(cell.strip() for cell in row) ]

# Print results
for r in clean_rows:
    print(r)