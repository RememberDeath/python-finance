print('Enter the phrase to translate into Pig Latin:')
message = input()
words = message.split()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y')
pigLatin = []
for word in message.split():
    if word[0] in VOWELS:
        pigLatin.append(word + 'yay')
    else:
        pigLatin.append(word[1:] + word[0] + 'ay')
print(' '.join(pigLatin))   
