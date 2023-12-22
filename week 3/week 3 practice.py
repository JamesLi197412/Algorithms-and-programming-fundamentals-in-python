a_list = []

count  = 0
while count < 5:
    a_list.append(count)#a_list[count] = count(wrong---list assignment index out of range)
    count = count + 1

print(a_list)

# Task 2: Lists

List = []
for i in range(5):
    number = int(input('Enter a Number: '))
    List.append(number)

print(List)

# Task 4: List of Lists, Tables and References

lines = int(input('How many lines of number would you like: '))
Table = []

for i in range(lines):
    List = input('Enter some numbers: ')
    List = List.split(' ')
    for j in range(len(List)):
        List[j] = float(List[j])

    Table.append(List)

print(Table)


