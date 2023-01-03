'''a=input("Enter The String")

if(len(a)%2==0):
    print("odd")
else:
    print("Even")
    '''
string=input("Enter The String\n")
s=string.split()
for i in s:
    if len(i)%2==0:
        print(i)