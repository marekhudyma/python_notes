x = 0
while x < 5:
    print(x)
    x += 1
else:
    print(f"End {x}")

x = [1,2,3,4,5,6,7,8,9,0]
for item in x:
    # comment => IndentationError: expected an indented block
    pass # nothing

for item in x:
    if item % 2 == 0:
        continue
    print(item)
    if item == 5:
        break