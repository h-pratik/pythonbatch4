def fibo(x):
    a=[]
    b = 0
    c =1
    for i in range(0,x):
        a.append(b)
        b,c = c,b+c
    return a
a = int(input("Enter the number of terms you want in Fibonacci Series: "))
for i in fibo(a):
    print(i)
