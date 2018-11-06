def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b

a=int(input("Enter a : \n"))
b=int(input("Enter b : \n"))
op=input("Enter operation :\n")
if(op=='+'):
    res=add(a,b)
elif(op=='-'):
    res=sub(a,b)
elif(op=='*'):
    res=mul(a,b)
elif(op=='/'):
    res=div(a,b)
else:
   print("Invalid operation")
   exit()
print(a," ",op," ",b," = ",res)

