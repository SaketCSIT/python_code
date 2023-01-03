a=input("Enter The String\n")
rev=""
i=a
for x in a:
    rev=x+rev
print(rev)

if i==rev:
    print("String Is Palindrome")
else:
    print("Not PAlindrome")