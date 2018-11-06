def dec_bin(n,s):
    if(n>1):
        s=dec_bin(n//2,s)
    s+=str(n%2)
    return s
s=''
n=int(input("Enter decimal :\n"))
print("Binary representation is : ",dec_bin(n, s))
    