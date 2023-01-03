'''num=int(input("Enter The Number"))
flag = False

if num > 1:

    for i in range(2, num):
        if num % i == 0:
            
            flag = True
            
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    '''
# Another Method Of ptime
a=int(input("Enter The Number"))

for x in range(2,a):
    if a%2==0:
        print("Not A prime")
        break
else:
    print("Prime Number")