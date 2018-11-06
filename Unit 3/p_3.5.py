def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

a=int(input("Enter a"))
b=int(input("Enter b"))
gcd_ab=gcd(a,b)
lcm_ab=(a*b)//gcd_ab
print("GCD : ",gcd_ab)
print("LCM : ",lcm_ab)