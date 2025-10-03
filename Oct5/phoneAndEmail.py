import pyperclip, re

phone_re = re.compile(r'''(
	(\d{3}|\(\d{3}\))? # area code
	(\s|-|\.)? # separator
	(\d{3}) # first 3 digits
	(\s|-|\.) # separator
	(\d{4}) # last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
	)''', re.VERBOSE)
email_re = re.compile(r'''(
	[a-zA-Z0-9._%+-]+  # Username
	@  # @ symbol
	[a-zA-Z0-9.-]+  # Domain name
    (\.[a-zA-Z]{2,4})  # Dot-something
    )''', re.VERBOSE)
text = str(pyperclip.paste())

matches = []

for groups in phone_re.findall(text):
    

   
    phone_parts = [groups[1], groups[3], groups[5]] 
    
    
    phone_num = '-'.join(filter(None, phone_parts))
    
   
    if groups[8]: 
        # Indented twice (this line belongs to the 'if' statement)
        phone_num += ' x' + groups[8]

    
    matches.append(phone_num)


for groups in email_re.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

