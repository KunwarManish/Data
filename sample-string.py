stg = 'Manish said, "I\'m busy today".'
print(stg)


# String with multiple lines
stg1 = ''' Hey there ! 
Welcome to Kathmandu'''
print(stg1)

st = "Kathmand u" # space also count
print(len(st))

print(st[5])

str = "lastdoor"
for i in str:
    print(i, end="")

sr = "Simplilearn"
print(sr[0:5])
print(sr[:5])
print(sr[5:])
print(sr[2:5])

string = "Welcome to Simplilearn"

print(string.upper())
print(string.lower())

print(string.find('S'))
print(string.index('S'))

print(string.find('l'))
print(string.index('l'))

print(string.split(" "))

x = string.split(' ')
print(x)

print(string.replace("Simplilearn","Python Tutorial"))

print(string.rpartition(" to "))


str1 = "good"
str2 = "morning"
str3 = str1 + " " +str2
print(str3)

print(str1 + " " +str2)

string1 = "Hey"
string2 = "there"
string3 = "all"
string4 = "{} {}, {}!".format(string1,string2,string3)
print(string4)



