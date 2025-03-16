class CheeseBorderMixin:
     def __init__(self, height: int):
         self.height = height
 
     def add_cheese_border(self):
         print("Сырный борт активирован!")
         print(f'Сырный борт, высотой {self.height} мм активирован!')
 
 class ThinkCrustMixin:
     def __init__(self, thickness: int):
         self.thickness = thickness
     def add_thin_crust(self):
         print("Тонкое тесто активировано!")
         print(f'Тонкое тесто, толщиной {self.thickness} мм активировано!')
 
 
 ######################
 @@ -29,17 +34,6 @@ def add_thin_crust(self):
 # 2. Нам нужна "мутация" - пицца с сырным бортом. Делаем экземпляр класса PizzaCheeseBorder
 
 class PizzaCheeseBorder(Pizza, CheeseBorderMixin):
     def __init__(self, size: int):
         super().__init__(size)
         self.add_cheese_border()
 
 # 3. Пирог с сырным бортом и тонким тестом
 class PieCheeseBorderThinCrust(Pie, CheeseBorderMixin, ThinkCrustMixin):
     def __init__(self, size: int):
         super().__init__(size)
 
 
 p = PieCheeseBorderThinCrust(30)
 print(p.size)
 p.add_cheese_border()
 p.add_thin_crust()
     def __init__(self, size: int, height: int):
         Pizza.__init__(self, size)
         CheeseBorderMixin.__init__(self, height)