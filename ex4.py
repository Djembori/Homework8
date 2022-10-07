n = 0
sum = 0
max = 1
min = 0
while n != 7:
    n = int(input('Enter the number: '))
    sum += n
    if n > max:
        max = n
    elif n < min or min == 0:
        min = n
    else:
        print('Good bye!')
print(f'Sum of numbers: {sum}')
print(f'Minimum of numbers: {min}')
print(f'Maximum of numbers: {max}')