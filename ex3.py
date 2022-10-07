n = 0
while n != 7:
    n = int(input('Enter number : '))
    if n == 7:
        print('Good Bye! ')
    elif n > 0:
        print('Number is positive ')
    if n < 0:
        print('Number is negative ')
    if n == 0:
        print('Number is equal to zero ')