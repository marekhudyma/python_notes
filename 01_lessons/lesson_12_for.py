my_iterable = [1, 2, 3, 4, 5, 6]

for num in my_iterable:
    if (num % 2 == 0):
        print(num)
print(len(my_iterable))

for letter in "Hello world":
    print(letter)

mylist = [(1,2), (3,4), (5,6), (7,8)]
for item in mylist:
    print(item)

# tuple unpacking
# for (a,b) in mylist:
for a,b in mylist:
    print(a)
    print(b)

d = {"k1": 1, "k2": 2, "k3": 3, "k4": 4}
# prints keys only
for item in d:
    print(item)

for item in d.items():
    print(item)

for key, value in d.items():
    print(f"key={key}, value={value}")

for key in d.keys():
    print(value)
for value in d.values():
    print(value)
    
