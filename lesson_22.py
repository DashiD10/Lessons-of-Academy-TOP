class Person:
    pass

p1 = Person()
p2 = Person()

print(p1, p2) #<__main__.Person object at 0x0000021D9C906A50> <__main__.Person object at 0x0000021D9CB7CCD0>

p1.name = "Филлип"
p2.name = "Джордж"

print(p1.name, p2.name) #Филлип Джордж