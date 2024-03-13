#
# Output test
# Regina 
#

# 1. Input 
x1 = int(input('Type x1:')) 
x2 = int(input('Type x2:')) 
op = input('Operator: ')

# 2. Process
if op == '+':
    sum = x1+x2
elif op == '-':
    sum = x1-x2

# 3. Output
print(f'Result : {sum}')
