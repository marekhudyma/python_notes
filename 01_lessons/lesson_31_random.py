import math
help(math)

print(math.floor(4.35))
print(math.ceil(4.35))
print(round(4.35))
print(round(5.5))
print(math.pi)

from math import pi
print(pi)
print(math.inf)
print(math.nan)

# Numpy # great library for math operations
# https://numpy.org/

print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(10))
print(math.degrees(pi/2))
print(math.radians(180))

import random
print(random.randint(0, 100))

# make random deterministic
random.seed(101)
print(random.randint(0,100)) # 74
print(random.randint(0,100)) # 24
print(random.randint(0,100)) # 69
print(random.randint(0,100)) # 45
print(random.randint(0,100)) # 59

mylist = list(range(0, 20))
print(mylist)
randomElement = random.choice(mylist)
print(randomElement)

# sample with replacement
print(random.choices(population=mylist, k=10)) # [13, 4, 4, 5, 13, 4, 19, 1, 3, 1]

# sample without replacement (repetition)
print(random.sample(population=mylist, k=10)) # [17, 11, 6, 15, 10, 3, 16, 12, 19, 18]

random.shuffle(mylist)
print(mylist)

print(random.uniform(a=0, b=100)) # 74.44690143237648

print(random.gauss(mu=0, sigma=1))
