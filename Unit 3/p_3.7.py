def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

n=int(input("Enter n"))
fib_list=[str(fib(i)) for i in range(0,n+1)]
list_f=','.join(fib_list)
print(list_f)
        
