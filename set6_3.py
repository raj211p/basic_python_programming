n=int(input('Enter the number of values in the Fibonacci sequence to be displayed: '))


def fibonacci(x,y,c):
  if c==n-1:
    print(y)
    return 0
  else:
     print(x)
     temp=y
     y=x+y
     x=temp
     return fibonacci(x,y,c+1)


fibonacci(0,1,0)
   