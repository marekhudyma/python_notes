s = set()
s.add(1)
s.add(2)
print(s)
s.clear()
s = {1,2,3}
print(s.copy())

print({1,2,3}.difference({2}))
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1)

s1 = {1,2,3}
s2 = {1,4,5}
s1.intersection_update(s2)
print(s1)

print({1,2}.isdisjoint({1,2,3})) # False
print({1,2}.issubset({1,2,3})) # True
print({1,2,3}.issubset({1,2})) # False

print({1,2}.symmetric_difference({1,2,3}))
print({1,2}.union({1,2,3}))

s1 = {1,2,3}
s2 = {1,4,5}
s1.update(s2)
print(s1)