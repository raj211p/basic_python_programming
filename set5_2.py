n=int(input('Enter a number: '))

sum=1
for i in range(2,n//2+1):
   if n%i==0:
       sum+=i

if sum==n:
  print('It is a perfect number.')
else:
  print('It is not a perfect number.')