# pylint - library reports possible code issues
# unittest - testing
# pip install pylint

'''
A very simple script
'''

def myfunc():
    '''
    A simple function
    '''
    first = 1
    second = 2
    print(first)
    print(second)


myfunc()

# pylint lesson_24_lint.py
# ************* Module lesson_24_tests
# lesson_24_lint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# lesson_24_lint.py:6:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# lesson_24_lint.py:7:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# lesson_24_lint.py:9:6: E0602: Undefined variable 'B' (undefined-variable)

# Your code has been rated at 6.67/10 (previous run: 0.00/10, +6.67)

