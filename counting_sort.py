from numpy import random

size=30
input = random.randint(10, size=(size))
print("Random array\n",input)

count = [0]*10
for i in input:
    count[i] += 1
print("Count\n",count)

c = 0
string = ""
for j in count:
    string+=(str(c)*j)
    c+=1

arr = [None]*size
c = 0
for x in string:
    arr[c] = int(x)
    c+=1
print("Sorted array\n",arr)
