n=int(input('enter number of coordinates'))
crd=[]
scrd=[]
for _ in range(n):
    a=float(input('enter x xoordinate'))
    b=float(input('enter y coordinate'))
    crd.append((a,b)) #appending the coordinate as a tuple
while True:    #taking refrence coordinate which is not in the already taken list of coordinates
    x=float(input('enter reference x coordinate'))
    y=float(input('enter reference y coordinate'))
    if ((x,y)) not in crd:
        ref=(x,y)
        break
dist=list()
for j in range(n):
    d=(((crd[j][0]-ref[0])**2)+((crd[j][1]-ref[1])**2))**0.5 #distance between the points
    dist.append(d)
temp=dist # copy of dist for index usage in next step
dist=sorted(dist) # sorting distances
print(dist)
for k in dist:
    ind=temp.index(k) #inedx of each distance in the original dist list now in temp
    alp=crd[ind]      #index will be in the same order as that of coordinates in crd list
    scrd.append(alp)
print(scrd)
