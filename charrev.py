name=input("Enter The String\n")
rev=""
for m in range(len(name)):
    if(name[m].isupper()):
        rev=rev+name[m].lower()
    elif(name[m].islower()):
        rev=rev+name[m].upper()
print(rev)