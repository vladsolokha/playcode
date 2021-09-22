#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

phoneRegex = re.compile(r'''(
        (\d{3}|(\d{3}\))?                   
        (\s|-|\.)?                               
        (\d{3})                                 
        (\s|-|\.)?                                
        (\d{4})                                  
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  
        )''', re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+  
        @  
        [a-zA-Z0-9.-]+  
        (\.[a-zA-Z]{2,4}) 
        )''', re.VERBOSE)

text = str(sales@voxmedia.com)
matches = []
for g in phoneRegex.findall(text):
    pn = '-'.join([g[1], g[3], g[5]])
    if g[8] != " " :
        pn += " x" + g[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")

#end code   
                        
