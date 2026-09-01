#Q8. Consider a CSV ( cones.csv ) with cone id, x, y, colour (blue or yellow) per row
#Sort the rows by distance from the origin. Write two new CSVs, one per colour,
# keeping the sorted order. Then find the midpoint between every blue cone and
# its nearest yellow cone and write those midpoints to centreline.csv.
import csv
import math
#cones.csv--> (id,x,y,colour)

def bubble_sort(l):  # this bubbble sort is only applicable to list having distance as 1st element
    for i in range(len(l)-1):
        for j in range(len(l)-1-i): #from the last, taking 2 elements as a time
            if l[j][0]>l[j+1][0]:
                l[j],l[j+1]=l[j+1],l[j] # swapping elements based on greater value
            
myfile=open("cones.csv","r")
reader=csv.reader(myfile)
file2=open("blue_cones.csv","w",newline="") #csv for blue cones
file3=open("yellow_cones.csv","w",newline="")#csv for yellow cones
writer2=csv.writer(file2)
writer3=csv.writer(file3) #creating writer objects
l1=[]      #blue
l2=[]      #yellow      # lists for stroing cones data based on colour for later sorting
for i in reader:
    d=math.sqrt(int(i[1])**2+int(i[2])**2)#distance of each point from the origin
    if i[3]=="blue":
        l1.append((d,i[0],i[1],i[2],i[3]))
    elif i[3]=="yellow":
        l2.append((d,i[0],i[1],i[2],i[3]))  
bubble_sort(l1)
bubble_sort(l2)
for i in l1:
    writer2.writerow(i) 
for i in l2:
    writer3.writerow(i)   # storing data in sorted order in different csv files based on colour
myfile.close()
file2.close()
file3.close()

# accessing and comparing blue and yellow cones to find midpoints
bfile=open("blue_cones.csv","r")
yfile=open("yellow_cones.csv","r")
breader=csv.reader(bfile)
yreader=csv.reader(yfile)
midpoint_list=[] #to store msipoints
for i in breader:
    yfile.seek(0)# in order to come back to the strt of the yellow cones file after readin once in next steps
    small=9999999999   #use python 'inf' value instead, it means +ve infinity
    for j in yreader:     #new storage formats in bfile and yfile -> (d,id,x,y,colour), x-2 indx, y-3indx
        d=math.sqrt((int(i[2])-int(j[2]))**2+(int(i[3])-int(j[3]))**2) #distnace b/w blue and yellow cones
        if d<small:      #we need shortest distance between them, therefore applying this method
            small=d
            xm=(int(i[2])+int(j[2]))/2 #midpoint x coordinate
            ym=(int(i[3])+int(j[3]))/2 #midpoint y coordinate
    midpoint_list.append((xm,ym))  #can append directly as each individual blue and yellow coordinates are already sorted
bfile.close()
yfile.close()
mid_file=open("centreline.csv","w",newline='')
mid_writer=csv.writer(mid_file)
for i in midpoint_list:
    mid_writer.writerow(i)
mid_file.close()
