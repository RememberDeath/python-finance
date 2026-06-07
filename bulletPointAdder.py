import pyperclip
text = pyperclip.paste() #Get the text from the clipboard
#ToDo: Separate lines and add stars
lines = text.split('\n') #Split the text into lines
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] #Add a star and a space at the beginning of each line
text = '\n'.join(lines) #Join the lines back into a single string
pyperclip.copy(text) #Copy the text to the clipboard