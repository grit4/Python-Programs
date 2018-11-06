def count(str):
    char={}
    words={}
    for i in str:
        if i in char.keys():
            char[i]+=1
        else:
            char[i]=1
    w=str.split()
    for i in w:
        if i in words.keys():
            words[i]+=1
        else:
            words[i]=1
    return char,words

s=input("Enter input")
c,w=count(s)
print("Frequency of characters : ")
print(c)
print("Frequency of words : ")
print(w)

        
    