my_list = [1, 2, 3]
help(my_list.pop())

def name_of_function(name ):
    '''
    Some method
    :return:
    '''
    print(f"hello {name}")
    return 2

name_of_function("John")

def myfunc(a, b, c=0, d=0):
    return sum((a, b, c, d)) * 0.05

myfunc(40, 60)

def myfunc2(*args):
    return sum(args) * 0.05

myfunc2(40, 60)

def myfunc3(*args):
    for item in args:
        print(item)

myfunc3(40, 60)

def myfunc4(**kwargs): # accepts dictionary
    print(kwargs)
    if('fruit' in kwargs):
        print(f'My fruit of choice is {kwargs["fruit"]}')
    else:
        print('I did nof find friut of choice')
myfunc4(fruit='apple', vegetable='tomato')


def myfunc5(*args, **kwargs):
    print(args)
    print(kwargs)

myfunc5(1,2,3, fruit="banana")