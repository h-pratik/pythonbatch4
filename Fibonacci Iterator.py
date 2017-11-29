def fibo(a):
    b=0
    c=1
    d = []
    while a!=0:
        d.append(b)
        b,c = c,b+c
        a-=1
    check_and_print(d)
def check_and_print(d):
    a = iter(d)
    while True:
        try:
            b=next(a)
        except StopIteration:
            break
        else:
            print (b)
a = int(input("Enter the number of terms you want in Fibonacci Series: "))
fibo(a)



