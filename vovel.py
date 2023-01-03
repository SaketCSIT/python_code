a=input("Enter The String\n")
ls=['a','e','i','o','u','A','E','I','O','U']
count=0
for x in a:
    if x in ls:
        print(x , len(x))
        