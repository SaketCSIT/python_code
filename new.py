'''
print(a,'+' ,b, '=',a-b)
variable =int(input("")).
a=float(input('Enter The Number\n'))
if a>=60:
    print("AIML")
elif a>=50 or a>40:
    print("medium brach")
else:
    print("not eli")
|x=2
s=int(input("How many times"))
for y in range(1,s):
 |# String
name=input('Enter Your Name')
print("Hello" , name)

a=float(input("Enter The Number\n"))
print(round(a))
|=10
for x in range(a):
    a=a-1
    for x in range(a):
        print("*", end='')
print("")
a=a+b
b=a-b
a=a-b
|array=[10,20,50,80]
print("Before Array", array)

array[1]=array[1]+array[2]
array[2]=array[1]-array[2]
array[1]=array[1]-array[2]
print("After Array" ,array)
'''
'''array=[10,50,60]
out=array.append(45)
print(array)
'''
'''array=[2,3,0]
for x in array:
    if x%2==0:
        print()
    else:
        print("no")
'''
'''a=int(input("Enter The Number"))
for x in range(1,10+1):
    out=a*x
    print(out)
'''
'''a=['df','ssd',23]
a.pop(1)
print(a)'''
'''arr=["saket",348,"Sas"]
print(arr.index("Sas"))'''


'''arra=[34,34,67,89]
print(arra.count(34))'''
'''
ls=['vehicle','objects','human','water']
slc=ls[10:0:-2]
print(slc,type(slc))'''
'''b=int(input("Enter the rows"))
count=65
for x in range(1,b+1):
    for z in range(x):
        print(chr(count),end="")
        count+=1
    print(" ")
    '''
'''a=int(input("Enter The Number"))
rev=0
while a>0:
    rev=(rev*10)+a%10
    a=a//10
print(rev)
'''
'''array=[10,20]
z=0
for x in range(0,len(array)):
    z=z+array[x]
print("Sum Is" , z)
'''
'''
name=input("Enter The Name")
rev=""
for x in range(len(name)):
    if(name[x].islower()):
        rev=rev+name[x].upper()
    elif(name[x].isupper()):
        rev=rev+name[x].lower()
    else:
        rel=rel+name[x]
print(rev)'''

'''a=25
b=2
print(a//b)


a=input("Enter The string")
count=0
'''
a=input("Enter")
ls=['a','e','i','i','o','u']
for x in a:
    if x in ls:
        print(x)
    print(len(x))
