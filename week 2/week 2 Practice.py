import random
# Task 1: Real Roots
# ax^2+bx+c =0
import math  # Import the math library

a = int(input('Input the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('There is no real roots')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('The one real root is: ', x1)
    print('The other real root is: ', x2)

# Task 2: Looping
# Displaying the interesting number

number_re = input('Please enter the largest number:')

maxDigits = len(number_re)  # len can not be used for the integer, only strings

number = 0

while number <= (int(number_re)):  # Can not compare the integers and string
    difference = maxDigits - len(str(number))
    if difference >= 0:
        number = '0' * difference + str(number)
    print(number)
    number = int(number) + 1

# Task 3: Three Special Categories of Lists
L = input('Please give a list of postive numbers:')

# print(L.split(','))
L = L.split(',')
L = list(map(int, L))
# print(L)
a = L[0]
b = L[0]  # Initialise

# To find the maximum number a in L list
for i in range(len(L)):
    if L[i] >= a:
        a = L[i]

# To find the minimum number b in L list
for i in range(len(L)):
    if L[i] <= b:
        b = L[i]

print('The maximum number in List is: ', str(a))
print('The minimum number in List is: ', str(b))

d = a - b

if d == 0:
    print('L has a narrow range')
elif d <= 100 and d > 0:
    print('l has a normal range')
else:
    print('L has a wide range')


# Task 4: Times tables and nested loops
x = 1


while x<=12:
    y = 1
    while y<=12:
        R =x*y
        print(x,'*',y,'=',R)
        y=y+1

    x+=1


### Workshop
# Task 1: Flippling Coins
n= int(input('How times would you like to flip the coni? '))
heads = 0
tails = 0
other = 0

for i in range(n):
    L=random.randrange(0,3,1)
    if L ==0:
        print('The coin came up heads')
        heads +=1
    elif L == 1:
        print('The coin came up tails')
        tails +=1
    else:
        print('The coin came up other')
        other+=1
print('number of heads occur is: ',str(heads))
print('number of tails occur is: '+str(tails))
print('number of other occur is: '+str(other))



print('Ratio of heads to total coin flips is: ',str(heads/n))
print('Ratio of tails to total coin flips is: '+str(tails/n))
print('Ratio of other to total coin flips is: '+str(other/n))

# Task 2_2(B): Operations on sequences of integers
i =int(input('Where should i start? '))
end=int(input('Where should i stop? '))
total = 0

for k in range(i,end+1,1):
    total = 3*k+total

print('The result for sum of 3i from',str(i),'to',str(end),'is:',str(total))

# Task 2_2(C): Operations on sequences of integers
i =int(input('Where should i start? '))
end=int(input('Where should i stop? '))
z = int(input('Valid i balues are those dibisible by...'))
total = 0


for k in range(i,end+1,1):
    if k%3 ==0:
        total = 2*k**2+4*k+total


print('The result for sum of 2i^2+4i from',str(i),'to',str(end),'is:',str(total))

# Task 2_2(D): Operations on sequences of integers

start =int(input('Where should i start? '))
end = int(input('Where should i stop? '))
total = 0

i= start
while i <=end:
    j=1
    while j<=i:
        total = total+4*j+2*i**2
        j+=1
    i+=1




print('The result for sum of the sums of 2i^2+4j from',str(start),'to',str(end),'is:',str(total))



