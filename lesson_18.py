# Функции. Области видимости. Замыкания. Декоратор. 

a = 2

def foo():
    a = 3
    print(f' foo = {a}')

def foo2():
    a = 4
    print(f' foo2 = {a}')

def foo3():
    print(f' foo3 = {a}')
          
print(a)
foo()
foo2()
foo3()