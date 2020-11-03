# создание классов с помощью type

d = type('D', (object,), {'x': 5, 'y': 6})

print(d)
print(d.__class__)
print(d.x)
print(d.y)
print('*************')
print('*************')


# можно объявлять класс внутри функции

def a():
    class A:
        x = 5

    return A


z = a()
print(z)
print(z.x)
print('*************')
print('*************')

nc = type('NewClass', (object,), {'a': 5, 'b': 7})
print(nc)
ncc = nc()
print(ncc)
print('*************')
print('*************')

MyClass1 = type('MyClass1', (), {'text': 'Python'})
print(MyClass1)
print(MyClass1.text)
MyClass2 = type('MyClass2', (MyClass1,), {})
print(MyClass2)
print(MyClass2.text)
mc2 = MyClass2
def func(self):
    print(self.text)

MyClass22 = type('MyClass22', (MyClass1,), {'func': func})
mc22 = MyClass22()
print(mc22)
print(mc22.text)
mc22.func()
