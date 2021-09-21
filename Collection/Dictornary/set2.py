# Initializing dictionary 1
dic1 = { 'Name' : 'Nandini', 'Age' : 19 }
  
# Initializing dictionary 2
dic2 = { 'ID' : 2541997 }
  
# Initializingd sequence
sequ = ('Name', 'Age', 'ID')

# Initializing list sequence
seqList = ["a", 'v', 'c']

print("Dictonary 1 ", dic1)
print("Dictonary 2 ", dic2)

dic1.update(dic2)
print("Update with dic2 ", dic1)

fromKeys = dict.fromkeys(seqList)
print(fromKeys)



#creating new defalut dictornary
newDict = dict.setdefault("default")
print("New Dictonary ", newDict)
  