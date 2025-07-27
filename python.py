num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
op = input('Enter an operation (+, -, *, /): ')

try:
    n1 = float(num1)
    n2 = float(num2)
except ValueError:
    print('Invalid input: Please enter valid numbers.')
    exit()

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2
elif op == '/':
    if n2 == 0:
        print('Error: Division by zero')
        exit()
    result = n1 / n2
else:
    print('Invalid operation')
    exit()

print(f'{n1} {op} {n2} = {result}')
