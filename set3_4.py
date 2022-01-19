c1=int(input('No. of students in the first class: '))
c2=int(input('No. of students in the second class: '))
c3=int(input('No. of students in the third class: '))
s1=c1//5
s2=c2//7
s3=c3//6
r1=c1%5
r2=c2%7
r3=c3%6
last_grp=r1+r2+r3
print('Group sizes: \nGroup 1: ',s1,'\nGroup 2: ',s2,'\nGroup 3: ',s3)
print('Last group: ',last_grp)
