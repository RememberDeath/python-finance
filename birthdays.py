birthdays = {'Alice': 1990, 'Bob': 1985, 'Charlie': 1992}

while True:
    print('Enter a name (or "" to quit):')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(str(birthdays[name]) + ' is the birth year of ' + name)
    else:
        print('Name not found.')
        print('Enter the birth year of ' + name + ':')
        birth_year = input()
        birthdays[name] = int(birth_year)
        print('Birth year of ' + name + ' has been added.')