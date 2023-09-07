def check_scope():
    def do_local():
        test='local test'
    def do_non_local():
        nonlocal test
        test='non local test'
    def do_global():
        global test
        test='global test'
    test='default'
    do_local()
    print('test result: '+test)
    do_non_local()
    print('test result: '+test)
    do_global()
    print('test result: '+test)
    do_local()
    print('test result: ' + test)


check_scope()

print('test result: ' + test)
'''

#The code you've provided demonstrates how different scopes and the `local`, `nonlocal`, and `global` keywords affect variable assignments. Let's break down the code step by step:

```python
def check_scope():
    def do_local():
        test = 'local test'

    def do_non_local():
        nonlocal test
        test = 'non local test'

    def do_global():
        global test
        test = 'global test'

    test = 'default'

    do_local()
    print('test result: ' + test)  # Output: test result: default

    do_non_local()
    print('test result: ' + test)  # Output: test result: non local test

    do_global()
    print('test result: ' + test)  # Output: test result: non local test

    do_local()
    print('test result: ' + test)  # Output: test result: non local test

check_scope()

print('test result: ' + test)  # This will result in an error since 'test' is not defined in the global scope.


Here's what's happening in the code:

1. The `check_scope` function defines three nested functions: `do_local`, `do_non_local`, and `do_global`. These functions illustrate the different ways variables can be scoped.
2. `test` is assigned the value `'default'` in the `check_scope` function.
3. `do_local` function creates a local variable named `test` with the value `'local test'`, but this variable doesn't affect the outer `test`.
4. `do_non_local` function uses the `nonlocal` keyword to modify the `test` variable in the closest enclosing scope (in this case, the `check_scope` function).
5. `do_global` function uses the `global` keyword to modify the global `test` variable.
6. The program calls the nested functions and prints the `test` value after each call.
7. After calling `check_scope()` and all its nested functions, the final print statement outside the function attempts to print the global `test` variable. However, since the `do_global` function was called and the `test` variable was modified with the `global` keyword, this line will result in an error because `test` is not defined in the global scope.

To fix the error, you should define a global `test` variable before calling the `check_scope` function.
'''
