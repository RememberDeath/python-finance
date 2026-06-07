import pyperclip
text = pyperclip.paste() #Get the text from the clipboard
alt_text = '' #Create a new string for the alternating text
make_uppercase = False #Start with lowercase
for character in text:
    if make_uppercase:
        alt_text += character.upper() #Add the uppercase version of the character
    else:
        alt_text += character.lower() #Add the lowercase version of the character
    make_uppercase = not make_uppercase #Switch the case for the next character
pyperclip.copy(alt_text) #Copy the alternating text to the clipboard
print('Alternating text copied to clipboard:') #Inform the user that the text has been copied
print(alt_text) #Print the alternating text to the console