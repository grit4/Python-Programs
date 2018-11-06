def sum_n(n,sum):
    if(n==1):
        sum+=1
        return sum
    sum+=n
    return sum_n(n-1,sum)

sum=0
n=int(input("Enter n"))
print(sum_n(n,sum))
    