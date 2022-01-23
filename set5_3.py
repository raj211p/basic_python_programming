n=input('Enter a string: ')
i=0; flag=True
while i<len(n)//2 and flag==True:
  if n[i]!=n[(len(n)-1)-i]:
      flag=False
      print('It is not a palindrome.')
      break
  i+=1

if flag==True:
   print('It is a palindrome.')