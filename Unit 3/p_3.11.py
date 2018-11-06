power=lambda n:1 if n==0 else 2*power(n-1)

n=int(input("Enter power :"))
print("2^",n," = ",power(n))