array=[10,12,78,76,45]
max=array[0]
n=len(array)
for x in range(1,n):
    if array[x]<max:
        max=array[x]
    
print(max)

