#improved verison of Q5
'''l1=[1,2,3]
l1.insert(0,0)    ----->   output: [0,1,2,3]
print(l1)'''

hash_table=[[] for _ in range(10)] #creaing a hash table
n=int(input('enter no. of integers:'))
for _ in range(n):
    num=int(input('enter the integer:'))
    r=num%10 #finding the remainder
    if hash_table[r]==[]:
        hash_table[r].append(num) #inserting element into respective sublist if it is empty
    else:
        l1=hash_table[r] # accessing sublist of the hash table
        l=len(hash_table[r])
        low=0
        high=l-1
        while low<=high:    #applying binary searc method.
            mid=(low+high)//2
            if l1[mid]>num:
                high=mid-1
            elif l1[mid]<num:
                low=mid+1
            else:     
                low=mid   #inserting element into respective sublist, it will always be insrted at the low index
        hash_table[r].insert(low,num)
print(hash_table)
