def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

new_list = list(map(square, my_nums))
print(new_list)


def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]
names = ["Andy", "Eve", "Sally"]
print(list(map(splicer, names)))

def check_even(num):
    return num % 2 == 0

mynums = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)

def square2(num):
    result = num ** 2
    return result

def square3(num): return num ** 2

lambda num: num ** 2

square4 = lambda num: num ** 2
print(square4(2))

print(list((map(lambda num: num ** 2, [1, 2, 3, 4, 5]))))

print(list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5])))

print(list(map(lambda str: str[0], ["Andy", "Eve", "Sally"])))