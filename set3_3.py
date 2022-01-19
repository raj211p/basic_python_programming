import math
slat=float(input('Latitude of point A: '))
slon=float(input('Longitude of point A: '))
elat=float(input('Latitude of point B: '))
elon=float(input('Longitude of point B: '))

if slat<=90.0 and slat>=-90.0 and elat<=90.0 and elat>=-90.0:
        if slon<=180.0 and slon>=-180.0 and elon<=180.0 and elon>=-180.0:
                    slat=math.radians(slat)
                    slon=math.radians(slon)
                    elat=math.radians(elat)
                    elon=math.radians(elon)
                    dlambda=math.fabs(slon-elon)
                    temp=math.acos((math.sin(slat)*math.sin(elat))+(math.cos(slat)*math.cos(elat)*math.cos(dlambda)))
                    dist=temp*6371.01
                    print('Distance between A and B: ',dist,' km.')
else:
    print('Invalid coordinates!')