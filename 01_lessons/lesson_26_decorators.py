# def func():
#     return 1
#
# def hello():
#     return "Hello"
#
# greet = hello
#
# print(greet())
# print(hello())
#
# del hello
#
# print(greet())
# # print(hello()) # fails

#####################################################################

# def hello(name='Jose'):
#     print("The hello() function has been executed")
#
#     def greet():
#         return "\t this is the greet() func inside hello"
#
#     def welcome():
#         return "\t this is the welcome() func inside hello"
#
#     # print(greet())
#     # print(welcome())
#     # print("The is the end of the hello function")
#     if name == "Jose":
#         return greet
#     else:
#         return welcome
#
# my_new_func = hello("Jose")
# print(my_new_func())
# # print(hello())

#####################################################################
# def hello():
#     return "Hi Jose"
#
# def other(some_def_func):
#     print("Other code runs here!")
#     print(some_def_func())
#
# other(hello)

#####################################################################
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function')
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()