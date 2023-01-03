'''a=int(input("Enter The Number"))
sum=0
org=a
while a>0:
    sum=sum+(a%10)*(a%10)*(a%10)
    a=a//10
if org==sum:
    print("Number Is A Armstrong")
else:
    print("Not")'''

'''a=int(input("Enter Thje Number"))
sum=0
temp=a
while a>0:
    sum=(sum*10)+a%10
    a=a//10
if sum==temp:
    print("Yes")
else:
    print("no")

a=input("Enter The String\n")
rev=""
for x in range(len(a)):
    if a[x].isupper():
        rev=rev+a[x].lower()
    elif a[x].islower():
        rev=rev+a[x].upper()
    else:
        rev+rev+a[x]
print(rev)

a=int(input("Enter The Number"))

for x in range(2,a):
    if a%2==0:
        print("Number Is not Prime")
        break
else:
    print("Number is Prime")


a=int(input("Enter The Number\n"))
fac=1
while a>0:
    fac=fac*a
    a-=1
print(fac)
'''
a=[]
s=int(input("Enter The Range"))
for i in range(s):
    val=int(input("ente The ele"))
    a.append(val)
sum=0
for q in range(i):
    sum=sum+a[i]
print(sum)