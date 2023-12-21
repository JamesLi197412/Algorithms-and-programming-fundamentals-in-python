# Numberical Operations
x = int(input('Please input the value:'))
y = int(input('Please input the value:'))
Adder= x +y
print('The Sum is:',Adder)

Diff = x - y
print('The Difference is:'+str(Diff))

Time = x*y
print('The Product is:'+str(Time))

Power = x**y
print('The Power is:'+str(Power))

Remainder = x%y
print('The Remainder is:'+str(Remainder))

Division = x / y
print('The Division is:'+str(Division))

Integer_division = x//y
print('The Integer division is:'+str(Integer_division))

Comp= x>y
print('The X>Y is:'+str(Comp))

import math

print('The cos(X/Y) is:',math.cos(x/y))


# Temperature Conversion
Fah=int(input('Given the temperature in Fahrenheit? '))
Cel=(Fah-32)*5/9
print(' The temperature is ' + str(Cel)+' degrees Celsius')
print(' The temperature is ' ,str(Cel),' degrees Celsius')

#Finding The nth Root
import math  #Import the math library
x = int(input('Please enter a value for x:'))
n = int(input('Please enter a value for n:'))

log = math.log(x)
root = math.exp(log/n)
print('The',str(n)+'th','root of',x,'is',root)

#Flipping Coins
import random
p = float(input('What kind of bias do your coins have ? '))
for i in range(3):
    x=random.random() #Return the next random floating point number in the range [0.0, 1.0).
    if x > p:
        print('Coin flip',i+1,'has a value of heads: True')
    else:
        print('Coin flip',i+1,'has a value of heads: False')

# Strings
strings =input('Enter any string you like: ')

