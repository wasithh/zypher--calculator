bot_name : str = 'Zypher'
print(f'Hello! I\'m {bot_name}, to calculate please write one of the following add/subtract/multiply/divide')
while True:
    user_input: str = input('You: ').lower()
    
    if user_input in ('+', 'add'):
        print(f'sure we can do some additions')

        num1 : float = float(input('First Number = '))
        num2 : float = float(input('Second Number = '))
        print(f'{bot_name}: The sum is : {num1 + num2}')
    elif user_input in ('-', 'subtract'):
       num1 : float = float(input('First Number = '))
       num2 : float = float(input('Second Number = '))
       print(f'{bot_name}: The difference is : {num1 - num2}') 
    elif user_input in ('*', 'multiply'):
       num1 : float = float(input('First Number = '))
       num2 : float = float(input('Second Number = '))
       print(f'{bot_name}: The multiplication is : {num1 * num2}')
    elif user_input in ('/', 'divide'):
       num1 : float = float(input('First Number = '))
       num2 : float = float(input('Second Number = '))
       if num2 == 0:
           print('Sorry, can\'t divide by zero you dumbass')
       else:
           print(f'{bot_name}: The division is : {num1 / num2}')


    else: 
        print(f'sybau lil bro I only do maths')


