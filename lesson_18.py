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


# a = 2

def foo(a: str): 
#    a = local для foo
    print(f'foo до вызова foo2 {a}')

    def foo2():
        # позволит переписать а из foo
       return a
    return foo2

f2 = foo("апельсин") 
f3 = foo("банан")
orange = f2()   #Замыкание. 
banana = f3()
print(f' принт1 {orange}')
print(f' принт2 {banana}')

# f2 -> foo2 -> апельсин (local a)