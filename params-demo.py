def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def process(f1, f2, f3, f4, process_name):
    if process_name == 'add':
        print(f1(2, 3)) 
    elif process_name == 'subtract':
        print(f2(5, 3)) 
    elif process_name == 'multiply':
        print(f3(5, 3)) 
    elif process_name == 'divide':
        print(f4(15, 3))
    else:
        print('Invalid process name')


process(add, subtract, multiply, divide, 'add')
process(add, subtract, multiply, divide, 'subtract')
process(add, subtract, multiply, divide, 'multiply')
process(add, subtract, multiply, divide, 'divide')
process(add, subtract, multiply, divide, 'error')
