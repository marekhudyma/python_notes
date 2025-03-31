l = [1, 2, 3]
l.append(4)

print(l)
print(l.count(1))

l = [1, 2, 3]
l.append([4, 5])
print(l)  # [1, 2, 3, [4, 5]]

x = [1, 2, 3]
y = [4, 5]
x.extend(y)
print(x)  # [1, 2, 3, 4, 5]

l = [1, 2, 3, 4, 5]
print(l.index(2))

# print(l.index(1_000_000)) # ValueError: 1000000 is not in list

l = [1, 2, 3, 4, 5]
l.insert(2, 'inserted')
print(l)

last = l.pop();
print(l)
print(last)

first = l.pop(0);
print(l)
print(first)

l.remove('inserted')
print(l)

l = [1, 2, 3, 4, 3]
l.remove(3) # removes first
print(l)

l = [1, 2, 3, 4, 5]
l.reverse()
print(l)

l.sort()
print(l)