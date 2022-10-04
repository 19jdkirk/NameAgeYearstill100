def ask_Name():
    print('Whats your name?')
    name = input()
    print('How old are you?')
    age = input()
    years_Till_100 = 100 - int(age)
    print(f'Hello {name}, you are {age} years old and you are {years_Till_100} years away from turning 100 years old!')


ask_Name()
