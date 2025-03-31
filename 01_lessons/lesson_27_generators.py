# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result
#
# print(create_cubes(10))
#
# for x in create_cubes(10):
#     print(x)
########################################################################################
# def create_cubes(n):
#     for x in range(n):
#         yield x**3 # not storing in memory
#
# for x in create_cubes(10_000):
#     print(x)
#
# print(create_cubes(10_000)) # <generator object create_cubes at 0x1010f8270>
########################################################################################
# def gen_fibon(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b
#
# for x in gen_fibon(10):
#     print(x)
########################################################################################

def simple_gen():
    for x in range(3):
        yield x

# for number in simple_gen():
#     print(number)

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # StopIteration

s = 'hello'

for letter in s:
    print(letter)

#next(s) #TypeError: 'str' object is not an iterator

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))