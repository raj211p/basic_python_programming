print('Enter the temperature (Celsius): ')
tempc1=int(input())
tempf1=(1.8*tempc1)+32
print('\n',tempc1,' degrees Celsius=',format(tempf1,'.2f'),' degrees Fahrenheit. ')

print('Enter the temperature (Fahrenheit): ')
tempf1=int(input())
tempc1=(tempf1-32)/1.8
print('\n',tempf1,' degrees Fahrenheit=',format(tempc1,'.2f'),' degrees Celsius. ')