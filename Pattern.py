'''a=int(input("Enter The Digit\n"))
for x in range(a): 
    for z in range(x,a):
        print("",end=" ")
    for z in range(x+1):
        print("#", end=" ")
    print("")

a=int(input("Enter The Number"))    
for q in range(a,0,a-1): 
    for z in range(q,a):
        print("", end=" ")
    for z in range(q-1):
        print('', end=" ")
    print(" ")
'''''''''
rows=9
for i in range(1,rows+1):
    for j in range(rows-i+1):
        print(end="*")
    for j in range(i-1):
        print(end=" ")
    for j in range(i-1):
        print(end=" ")
    for j in range(rows-i+1):
        print(end="*")
    print()