d = {'k1': 1, 'k2': 2}

d2 = {x: x ** 2 for x in range(10)}
print(d2)

d2 = {k: v**2 for k,v in zip(['a', 'b'], range(10))}
print(d2)

for k in d.keys():
    print(k)

for k in d.values():
    print(k)