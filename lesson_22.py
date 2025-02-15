class Person:
    def __init__(self, name: str):
        self.name = name

    def say_my_name(self):
        print(f'Меня зовут {self.name}')

p1 = Person("Барак")
p2 = Person("Владимир")
p3 = Person("Дональд")

print(p1.name, p2.name, p3.name) #<__main__.Person object at 0x0000021D9C906A50> <__main__.Person object at 0x0000021D9CB7CCD0>
p1.say_my_name()
p1.say_my_name()
p1.say_my_name()

