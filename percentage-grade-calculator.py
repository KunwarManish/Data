
name = input('Enter student name : ')
fmarks = int(input('Enter full marks : '))
maths = float(input('Enter maths marks : '))
english = float(input('Enter english marks : '))
physics = float(input('Enter physics marks : '))
chemistry = float(input('Enter chemistry marks : '))
computer = float(input('Enter computer marks : '))

if maths > fmarks or english > fmarks or physics > fmarks or chemistry > fmarks or computer > fmarks:
    print('Ivalid marks inputed')
    print('Reenter the name and marks')

else:
    totalmarks = maths + english + physics + chemistry + computer
    percentage = (totalmarks/ (5 * fmarks)) * 100
    print(name, 'got', percentage, '%')
    
    if percentage >= 90 and percentage <= 100:
        print(name,'got A+ Grade')
    elif percentage >= 80 and percentage <= 90:
        print(name,'got A Grade')
    elif percentage >= 70 and percentage <= 80:
        print(name,'got B+ Grade')
    elif percentage >= 60 and percentage <= 70:
        print(name,'got B Grade') 
    elif percentage >= 50 and percentage <= 60:
        print(name,'got C+ Grade')   
    elif percentage >= 40 and percentage <= 50:
        print(name,'got D+ Grade') 
    elif percentage >= 30 and percentage <= 40:
        print(name,'got D Grade') 
    else:
        print(name, 'Failed in the Examination')   