s=[]
x=input('Enter some words (type \'end\' to specify the end of the list): ')
s.append(x)
while x!='end':
   x=input()
   if x!='end':
       s.append(x)

def myfilter(call,j):
   for s in j:
      if call(s): 
        yield s
lst=list(myfilter(lambda x: not x[0].isdigit(),s))
print(lst)


  