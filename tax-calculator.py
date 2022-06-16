totalamount = float(input('Enter the total amount of bill : '))
taxperamount = float(input('Enter the % charged for tax : '))
tax = totalamount * taxperamount/100
amount = totalamount + tax
print('Tax is', tax)
print('Amount to pay is', amount)



