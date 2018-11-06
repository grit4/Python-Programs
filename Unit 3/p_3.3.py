def remove_dupl(l):
    new_l=[]
    for i in l:
        if i not in new_l:
            new_l.append(i)
    return new_l

initial=[12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
newlist=remove_dupl(initial)
print("After removing duplicates : ",newlist)

            