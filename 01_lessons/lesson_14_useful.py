for num in range(10):
    print(num)

for num in range(5, 10):
    print(num)

for num in range(0, 10, 2):
    print(num)

print(list(range(10)))

index_count = 0;
for letter in 'abcde':
    print(f'At index {index_count}, letter is {letter}')
    index_count += 1

for item in enumerate('abcde'):
    print(item)

for index, letter in enumerate('abcde'):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']

for item in zip(mylist1, mylist2):
    print(item)

for a,b in zip(mylist1, mylist2):
    print(a)
    print(b)

print('x' in [1,2,3])
print('key' in {'key': 345})
print(345 in {'key': 345}.values())

print(min([1,2,3]))
print(max([1,2,3]))

from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0, 100))

result = input('Enter a number here:')
print(float(result))
print(int(result))