givenString = "ada"

newString = ''

for i in range(len(givenString), 0, -1):
    newString += givenString[i-1]

print(newString)

if(givenString == newString):
    print("Palendrome")
else:
    print("normal")