def cipher(str,s):
    new=''
    for i in str:
        if i.islower():
            t=97+(ord(i)-97+s)%26
            new+=chr(t)
        else:
            t=65+(ord(i)-65+s)%26
            new+=chr(t)
    return new

msg=input("Enter string to be encrypted")
n=int(input("Enter shift"))
print("Cipher text : ",cipher(msg,n))