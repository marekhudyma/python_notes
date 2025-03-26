#one.py
#
# print(__name__) # __main__  - this py file is run directly
#
# if(__name__ == "__main__"):
#     print("__main__")

def func():
    print("func() in one.py")

print("top level in one.py")

if(__name__ == "__main__"):
    print("one.py is being run directly")
else:
    print("one.py has been imported")