class MyDecor1:
    def __init__(self, f):
        print('before function')
        f()
        print('after function')

    def __call__(self):
        print('call')


@MyDecor1
def func1():
    print('function')


print('*************')


def mydecor2(func):
    def decorated(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result

    return decorated


print('*************')


def x(a, b):
    return a + b


xmydecor2 = mydecor2(x)
print(xmydecor2)
xmydecor2(5, 6)
print(xmydecor2(5, 6))

print('*************')


def y(a, b):
    return a * b


ymydecor2 = mydecor2(y)
print(ymydecor2(5, 6))

print('*************')


@mydecor2
def z(a, b):
    return a - b


print(z(5, 6))

print('*************')


@mydecor2
@mydecor2
@mydecor2
def w(a=5, b=6):
    return a / b


print(w())
print('*************')
print(w(10, 5))

print('*************')
print('*************')


def mydecorator3(hello='hello', bye='bye'):
    def internal(func):
        def decorated(*args, **kwargs):
            print(hello)
            result = func(*args, **kwargs)
            print(bye)
            return result

        return decorated

    return internal


@mydecorator3('one', 'two')
def aa(a=5, b=4):
    return a + b


print(aa())
print('*************')
print('*************')


def paragraf(func):
    def inner(*args, **kwargs):
        print('<p>')
        func(*args, **kwargs)
        print('</p>')

    return inner


@paragraf
def hello(text='I Love Python'):
    print('Hello', text)


hello()
print('*************')
print('*************')


def mytag(tagname='p'):
    def decorator(func):
        def inner(text):
            print(f'<{tagname}>')
            func(text)
            print(f'</{tagname}>')

        return inner

    return decorator


@mytag('p')
@mytag('b')
def hello(text):
    print('Hello,', text)


hello('My name is Al_Savva!')

print('*************')
print('*************')
print(hello.__name__)
print('*************')
print('*************')
from functools import wraps


def paragraf1(func):
    @wraps(func)
    def inner(text):
        print('<p>')
        func(text)
        print('</p>')

    return inner


@paragraf1
def hello(text):
    print('Hello!', text)


hello('I`m Python!')
print(hello.__name__)
