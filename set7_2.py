i=int(input('Enter the length of the array to be created: '))
arr=[]
print('Array elements: \n')
k=0
while k<i:
  x=int(input())
  arr.append(x)
  k+=1
  
def myreduce(call,j):
  n=j[0]
  for s in range(1,len(j)):
      n=call(n,j[s])
  return n

print('Largest element in the list: ')
print(myreduce(lambda x,y: x if x>y else y, arr))
print('Sum of the values: ')
print(myreduce(lambda x,y: x+y,arr))