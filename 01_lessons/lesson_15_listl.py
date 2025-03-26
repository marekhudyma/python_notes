mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

mylist = [num ** 2 for num in range(0, 11)]
print(mylist)

mylist = [num ** 2 for num in range(0, 11) if num % 2 == 0]
print(mylist)

celcius = [0, 10, 20, 34.5]
farenheit = [(9 / 5 * temp + 32) for temp in celcius]
print(farenheit)

results = [x if x % 2 == 0 else 'ODD' for x in range(10)]
print(results)

mylist = []
for x in [2,4,6] :
    for y in [1,10,1000] :
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)