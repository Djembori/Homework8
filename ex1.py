n1=int(input('Enter number : '))
n2=int(input('Enter number : '))
odd=0
even=0
sum9=0
for i in range(n1,n2+1):
    if i%2!=0:
        odd+=i
    if i%2==0:
        even+=i
    if i%9==0:
        sum9+=i
print("Sum of odd: ",odd)
print("Sum of even: ",even)
print("sum of multiples of 9: ",sum9)


