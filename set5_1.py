n=input('Enter a number: '); x=int(n)
l=len(n); n=int(n)
i=0; sum=0
while i<l:
  d=n%10; sum+=(d**l)
  n=n//10; i+=1
if sum==x:
  print('It is an Armstrong number.')
else:
  print('It is not an Armstrong number.')



