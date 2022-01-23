from math import sqrt
print('Equation: ax^2+bx+c')
print('Enter a, b, & c: ')
a=int(input())
b=int(input())
c=int(input())
D=float((b**2)-4*a*c)

if a==0:
  print('Equation: bx+c')
  print('Solution: x=',(-1*c/b))
elif D==0:
  print('The roots are real & equal.')
  print('x1=x2=',(-1*b/(2*a)))
elif D>0:
  print('The roots are real & distinct.')
  x1=((-1*b)-sqrt(D))/(2*a); x2=((-1*b)+sqrt(D))/(2*a); print('Roots: ',x1,', ',x2)
elif D<0:
  print('The roots are imaginary.')

