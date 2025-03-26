
str = "Marek"
print(str[1])
print(str[-1])

print("hello \nworld")
print("hello \tworld")
print(len("hello \tworld"))
print("abcdef"[2:]) # cdef
print("abcdef"[:2]) # ab
print("abcdef"[2:4]) # cd
print("abcdef"[::]) # abcdef
print("abcdef"[::2]) # ace - jump 2
print("abcdefghij"[::5]) # af - jump 5
print("abcdefghij"[2:3:5]) # c
print("abcdefghij"[::-1]) # jihgfedcba

print("String here {} them also {}".format("something1", "something2"))
print("String here {1} them also {0}".format("something1", "something2"))
print("String here {s1} them also {s2}".format(s1="something1", s2="something2"))

result = 100/77
print(result)
print("{r:1.3f}".format(r=result))
print("{r:10.3f}".format(r=result))

name = "Marek"
print("Hello, his ame is {}".format(name))
print(f"Hello, his ame is {name}")