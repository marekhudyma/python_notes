# myfile = open("not_existing_file.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'not_existing_file.txt'

myfile = open("myfile.txt")
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)

print(myfile.readlines())
myfile.close()

# auto close
with open("myfile.txt") as my_new_file:
    print(my_new_file.read())

# with open("myfile.txt", mode='w') as my_new_file: # io.UnsupportedOperation: not readable
#     print(my_new_file.read())

with open("myfile.txt", mode='a') as my_new_file: # io.UnsupportedOperation: not readable
    my_new_file.write("\nfourth")