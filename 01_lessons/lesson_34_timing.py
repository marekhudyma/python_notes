
def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))

print(func_two(10))

import time

# current time before code
start_time = time.time()
# run code
result = func_two(1_000_000)
# current time after code
end_time = time.time()

elapsed_time = end_time - start_time
print(elapsed_time) # in seconds
# precision is too small

import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=1_000_000))
# 8.676040624999999

stmt2 = '''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt2, setup2, number=1_000_000))
# 9.061378125