total_amount = int(input('Enter amount: '))
taxed_amount = total_amount + (total_amount * 20/100)
no_of_friends = int(input("Enter no of pepole : "))
amountperperson = taxed_amount/no_of_friends
print(f"Each person have to pay : {amountperperson}") 