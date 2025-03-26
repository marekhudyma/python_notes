my_list = [1, 2, 3]
my_list = ["String", 100, 3.2]
print(len(["String", 100, 3.2]))

my_list = ["1", "2", "3"]
print(my_list[1:])
anotger_list = ["4", "5"]
print(my_list + anotger_list)

my_list = ["1", "2", "3", "4", "5"]
my_list[0] = "one"
print(my_list)

my_list.append("6")
print(my_list)

print(my_list.pop()) # remove last element
print(my_list)

print(my_list.pop(0)) # remove last element
print(my_list)

new_list = [4, 3, 8, 1]
new_list.sort() # not returning anything
print(new_list)

print(new_list.sort()) # None - null in python
print(type(new_list.sort())) # <class 'NoneType'>
