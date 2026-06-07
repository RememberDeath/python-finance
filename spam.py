print("Hello there!\nHow are you?\nI\'m doing okay.") #\n is a newline character, \' is an escaped single quote, and \\ is an escaped backslash

print(r'The file is C:\some\name') #Raw string, ignores escape characters; good for file paths and regular expressions
print('Hello...\n\n...world!')
print('''Dear Alice,
I hope this email finds you well.
Best regards,
Bob''')
print("Dear Alice,\nI hope this email finds you well.\nBest regards,\nBob") #multi line string using \n for newlines instead of triple quotes