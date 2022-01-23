import sys
date=input('Enter a date: ')
dd,mm,yy=date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
m1=[1,3,5,7,8,10,12]
m2=[4,6,9,11]
if mm>12:
  print('Invalid date.')
  sys.exit()
if (yy%4==0 and yy%100!=0) or yy%400==0:
  if mm==2:
     if dd>=30:
           print('Invalid date.')
     elif dd<=29:
           print('Valid date.')
           if dd==29:
               print('Next date: 1/3/',yy);
           else:
                print('Next date: ',dd+1,'/',mm,'/',yy); 
if mm in m1:
   if dd<=31:
       print('Valid date.')
       if dd==31 and mm!=12:
              print('Next date: 1/',mm+1,'/',yy)
       elif dd==31 and mm==12:
              print('Next date: 1/1/',yy+1)
       elif dd<31:
              print('Next date: ',dd+1,'/',mm,'/',yy)
   else:
       print('Invalid date.')

elif mm in m2:
   if dd<=30:
       print('Valid date.')
       if dd==30:
           print('Next date: 1/',mm+1,'/',yy)
       else:
           print('Next date: ',dd+1,'/',mm,'/',yy)
   else:
       print('Invalid date.')

elif mm==2:
   if dd<=28:
      print('Valid date.')
      if dd==28:
           print('Next date: 1/3/',yy)
      else:
           print('Next date: ',dd+1,'/2/',yy)
   else:
           print('Invalid date.')