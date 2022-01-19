print('Enter a number: ')
num=int(input())
print('Digits (least significant first): ')
while num!=0:
    d=num%10
    print(d,'\n')
    num=num//10