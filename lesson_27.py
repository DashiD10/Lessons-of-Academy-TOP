

class Pizza:
    def __init__(self, size: int):
        self.size = size

class Pie:
    def __init__(self, size: int):
        self.size = size
    

class CheeseBorderMixin:
    def add_cheese_border(self):
        print('Сырный борт активирован')

class ThinkCrustMixin:
    def add_think_crust(self):
        print('Тесто активировано')


class PizzaCheeseBorder(Pizza, CheeseBorderMixin):
    def __init__(self, size: int):
        super().__init__(size)
        self.add_cheese_border()

class PieCheeseBorderThinCrust(Pie, CheeseBorderMixin, ThinkCrustMixin):
    def __init__(self, size: int):
        super().__init__(size)
        self.add_cheese_border()
        self.add_think_crust()

p = PieCheeseBorderThinCrust(30)
print(p.size)
p.add_cheese_border()
p.add_think_crust()