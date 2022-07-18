import random, os

nums ='1234567890'
letters = 'abcdefghijklmnopqrstuvwxyz'
capLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
specials = '@#$&%_()!?'
types = {'l': True, 'cl': True, 'n': True, 's': True}

def generatePassword(len):
    password = ''
    for _ in range(int(len)):
        while True:
            type = random.choice(list(types))	
            if types[type] == True:
                if type == 'l':
                    password += letters[random.randint(0, 25)]
                if type == 'cl':
                    password += capLetters[random.randint(0, 25)]
                if type == 'n':
                    password += nums[random.randint(0, 9)]
                if type == 's':
                    password += specials[random.randint(0, 9)]
                break
    return password

def togle(type):
    if types[type] == True:
        types[type] = False
    else:
        types[type] = True

history = []
while True:

    os.system('cls')
    print('Password Generator\n\n-c (config)\n-h (history)\n')
    x = input('How many characters in the password: ')

    if x.isnumeric():
        password = generatePassword(x)
        history.append(password)
        print('Password: '+ password)
        print(input('\nContinue:'))

    elif x.lower() == '-c':
        while True:
            togle_l = 'on' if types['l'] == True else 'off'
            togle_cl = 'on' if types['cl'] == True else 'off'
            togle_n = 'on' if types['n'] == True else 'off'
            togle_s = 'on' if types['s'] == True else 'off'

            os.system('cls')
            print(f'Password Generator Configs\n\na) LETTERS            ({togle_l})\nb) CAPITAL LETTERS    ({togle_cl})\nc) NUMBERS            ({togle_n})\nd) SPECIAL CHARACTERS ({togle_s})\n')
            config = input('->')

            if config.lower() == 'a':
                togle('l')
            elif config.lower() == 'b':
                togle('cl')
            elif config.lower() == 'c':
                togle('n')
            elif config.lower() == 'd':
                togle('s')
            else:
                break

    elif x == '-h':
        os.system('cls')
        print('Password Generator History\n')
        for password in history:
            print(f"'{password}'")
        input('->')

    else:
        break