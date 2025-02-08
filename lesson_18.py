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

# Счетчик, который помнит свое состояние и может принять стартовую позицию

def counter(start: int = 0, step: int = 1):

    position = start

    def tik():
        nonlocal position
        position += step
        return position
    
    return tik

counter_0_2 = counter(0, 2)
print(counter_0_2())
print(counter_0_2())
print(counter_0_2())


product_list = ["морковь", "картофель", "свекла", "свекла", "чеснок"]

def get_sorter():
    cach = []

    def sorter(data_list: list):
        nonlocal cach
        if cach and len(cach) == len(data_list):
            return cach
        
        cach = sorted(data_list)
        return cach
    
    return sorter
    
product_sorter = get_sorter()
print(product_sorter(product_list))
print(product_sorter(product_list))

product_list.append("лук")
print(product_sorter(product_list))
print(product_sorter(product_list))
    
 


from typing import Callable

product_list = ["морковь", "картофель", "свекла", "свекла", "чеснок"]

def use_built_in_func(func: Callable, data_list: list):
    print(func(data_list))

use_built_in_func(len, product_list)
use_built_in_func(sorted, product_list)
use_built_in_func(sum, [1, 2, 3, 4, 5])


def simple_decorator(func: Callable):
    def wrapper():
        print(f'Печать до вызова.')
        result = func()
        print(f'Печать после вызова.')

        return result

    return wrapper


@simple_decorator
def foo():
    return f'Результат foo'

@simple_decorator
def foo66():
    return f'Функция 66'

print(foo())
print(foo())
print(foo())

# foo_decorated = simple_decorator(foo, "Привет")
# result = foo_decorated()
# print(result)
    