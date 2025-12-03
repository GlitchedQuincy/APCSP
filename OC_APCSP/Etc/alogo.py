sum=0 
ML=[4,7,3,10,6]
for num in ML:
    sum=sum+num
print("The sum is:",sum)


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a%b == 0:
    print(a,"is divisible by",b)
else:
    print(a,"is not divisible by",b)


list=[4,12,3,7,6,10]
c=int(input("Enter a number:"))
i=0
for i in range(len(list)):
    if c == list[i]:
        print(c,"is present in the list")
    elif i < len(list)-1: 
        i=i+1
    else:
        print(c,"is not present in the list")
'''
if c in list:
    print(c,"is present in the list")
else:
    print(c,"is not present in the list")
'''


#ML already defined above
max=ML[0]
min=ML[0]
for num in ML:
    if num > max:
        max=num
    if num < min:
        min=num
print("The maximum number is:",max)
print("The minimum number is:",min)