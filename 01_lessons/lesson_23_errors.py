

# def add(n1, n2):
#     print(n1 + n2)
#
# add(10, 20)
#
# number1 = 10
# number2 = input("Please provide a number: ")
#
# try:
#     result = add(number1, number2)
# except:
#     print("Some error occurred")
# else:
#     print(f"Result={result}")
##########################################
# try:
#     f = open('testfile.txt', 'w')
#     f.write("write a test line")
# except TypeError:
#     print("There was a TypeError")
# except OSError:
#     print("OSError")
# except:
#     print("All other exceptions")
# finally:
#     print("I always run")
##########################################
def ask_for_int():
    while True:
        try:
            result = int(input("Please enter a number: "))
        except:
            print("whoops! That is not a number")
            continue
        else:
            print("Thank you!")
            break
        finally:
            print("End of try/except/finally")

ask_for_int()
