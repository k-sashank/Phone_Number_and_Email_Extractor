#Import required Libraries
import pyperclip, re
#Regular Expressions to detect Phone Numbers and Email Addresses
phoneRegex = re.compile(r'''((\s|\+|\.)?(\d{2}|\(\d{2}\))?(\s|-|\.)?(\d{10}))''', re.VERBOSE)
emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)
#List to store all the detected Phone Numbers and Email Addresses
matches = []
#Opening file.txt in read-mode
file = open('sample_text_file.txt', 'r')
#Loop to scan each line in the file
for each in file:
    #Loop to scan all the phone numbers in the line and appending them to matches
    for groups in phoneRegex.findall(each):
        phoneNum = groups[1] + groups[2] + groups[4]
        matches.append(phoneNum)
    #Loop to scan all the email ids in the line and appending them to matches
    for groups in emailRegex.findall(each):
        matches.append(groups[0])
#Conditional to check if we got at least one match
if len(matches) > 0:
    #Printing th data found
    print("Data Found: ")
    for i in range(0,len(matches)):
        print(matches[i])
        #Copying to clipboard
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
#Conditional in case nothing is found
else:
    print('No phone numbers or email addresses found.')
