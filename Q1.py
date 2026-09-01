n=int(input('enter an integer'))
l1=[]
d1={}
for i in range(n):
    a=input('enter a string').lower()
    l1.append(a)
for i in l1: #accessing string in list
    for j in i: # accessing each character in string
        if j in d1: #checking if its count already exists
            d1[j]+=i.count(j)
        else:
            d1[j]=i.count(j) #creating/starting count
print(d1)
#practicing git