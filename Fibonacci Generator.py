def fibo(a):
    b=0
    c=1
    while a!=0:
        yield(b)
        b,c = c,b+c
        a-=1
a = int(input("Enter the Number of terms you want in Fibonacci Series : "))
for i in fibo(a):
    print(i)
