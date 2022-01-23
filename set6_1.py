i=int(input('Enter the length of the array to be created: '))
lst=[]
print('Array elements: \n')
j=0
while j<i:
  x=int(input())
  lst.append(x)
  j+=1

def findmin(a):
  if len(a)==1:
     return a[0]
  else:
    return min(a[0],findmin(a[1:]))

print(findmin(lst),' is the smallest value in the list.')