num1 = int (input( 'Enter the 1st number : '))
num2 = int (input( 'Enter the 2nd number : '))
num3 = int (input( 'Enter the 3rd number : '))

if (num1 > num2):
    if (num1 > num3):
        print ('1st number is the largest number')
    else:
        print('3rd number is the largest number')
elif(num2 > num3):
    print('2nd number is the largest number')
else:
    print('3rd number is the largest number')
