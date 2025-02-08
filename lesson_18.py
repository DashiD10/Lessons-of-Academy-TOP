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

def product_sort(products: list):
    cach = []

    def sorter():
        nonlocal cach
        if cach and len(cach) == len(products):
            return cach
        
        cach = sorted(products)
        return cach
    
    return sorter
    
product_sorter = product_sort(product_list)
print(product_sorter())
print(product_sorter())

product_list.append("лук")
print(product_sorter())
print(product_sorter())
    
 
