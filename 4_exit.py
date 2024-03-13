#
# Exit test
# Regina 
#

sum = 0

while True:
    x1 = input('Type 1:')
    x2 = input('Type 2:')
    op = input('Operator:')

    if op == '+':
        sum = int(x1)+int(x2)
    elif op == '-':
        sum = int(x1)-int(x2)

    print(f'Result: {sum}')
    
    option = input('Do you want to continue? c for continue and s for stop:')
    if option == 'c':
        continue
    elif option == 's':
        break
    else:
        print('Wrong input, stopping the program')
        break

