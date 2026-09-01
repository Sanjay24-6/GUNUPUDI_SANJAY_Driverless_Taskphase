# A 2-D List is basically something like this -> [[],[],[],[]] (list inside of a list)
hash_table=[[] for _ in range(10)] #creaing a hash table
n=int(input('enter no. of integers:'))
for _ in range(n):
    num=int(input('enter the integer:'))
    r=num%10 #finding the remainder
    hash_table[r].append(num) #inserting element into respective sublist
print(hash_table)