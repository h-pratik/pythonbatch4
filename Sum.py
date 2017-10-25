def sum(x,a):
    sum=0
    i=0
    while(x!=0):
        sum=sum+a[i]
        x-=1
        i+=1
    return sum
        
print("Enter the amount of numbers: ");
x = int(input());
a=[]
t=0
for t in range(x):
    a.append(x)
print(a)
i=0
temp=x
while(x!=0):
    print("Enter the number: ")
    a[i] = int(input())
    x-=1
    i+=1
s=sum(temp,a)
print("The sum is", s)