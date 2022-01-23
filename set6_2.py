a=int(input('Base: '))
b=int(input('Exponent: '))
def pwr(a,b):
  if b==1:
   return a
  else:
   return a*pwr(a,b-1)

print(a,'^',b,'=',pwr(a,b))
