# Функции. Области видимости. Замыкания. Декоратор. 

# a = 2

# def foo():
#     a = 3
#     print(f'foo = {a}')

# def foo2():
#     global a
#     a = 4
#     print(f'foo2 = {a}')

# def foo3():
#     print(f'foo3 = {a}')
          
# print(a)
# foo()
# foo2()
# foo3()
# print(a)


a = 2

def foo(): 
    a = 3
    print(f'a после объявления переменной = {a}')

    def foo2():
        nonlocal a   # Позволяет обратиться к переменной из внешней функции foo
        a = 4
        print(f'a после объявления переменной = {a}')

    foo2()
    print(f'a после объявления переменной = {a}')

foo() 

bananas = print

bananas("Привет!")
bananas("Как дела?")

one = "один"
bir = one
odin = bir
print(odin)