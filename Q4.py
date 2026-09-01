r1=int(input('enter no. of rows in matrix 1:'))
c1=int(input('enter no. of columns in matrix 1:'))
r2=int(input('enter no. of rows in matrix 2:'))
c2=int(input('enter no. of columns in matrix 2:'))
if c1!=r2:
    print('matrix multiplication not possible')
else:
    m1=[]
    m2=[]
    for i in range(r1):
        a=[]
        for j in range(c1):
            a.append(int(input('enter element')))#taking in elements row by row
        m1.append(a) #appending the row
    for i in range(r2): # for matrix 2
        b=[]
        for j in range(c2):
            b.append(int(input('enter element'))) 
        m2.append(b)
    res = [[0] * c2 for _ in range(r1)] #creating a result matrix with initially all 0s
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j]+=m1[i][k]*m2[k][j] #multiplying each row with column  and adding to res which has all 0s
    print(res)                        #here m2[k] becasue wkt r2=c1
