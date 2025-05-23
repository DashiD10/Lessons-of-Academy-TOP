# class Counter: 
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return Counter(self.value + other.value)
# counter1 = Counter(5)
# counter2 = Counter(16)
# counter3 = counter1 + counter2
# print(counter3.value)

# class Counter1:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return Counter(self.value + other)
# counter4=Counter1(30)
# counter5=counter4 + 5
# print(counter5.value)

# class Counter2:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value+other
#     counter6=Counter2(8)

#     result=counter6+7
#     print(result)

# class Bool1:
#     def __init__(self, value):
#         self.value = value
#     def __bool__(self):
#         return self.value>0

# def test(bool1):
#     if bool1:
#         print(True)
#     else:
#         print(False)
        
# bool1=Bool1(-1)
# test(bool1)
# bool2=Bool1(6)
# test(bool2)

# class Num:
#     def __init__(self, value):
#         self.value = value
#     def __gt__(self, other):
#         return self.value > other.value
#     def __lt__(self, other):
#         return self.value < other.value
    
# num1=Num(3)
# num2=Num(6)

# if num1 > num2:
#     print("num1 > num2")
# elif num1 < num2:
#     print(num1 < num2)
# else:
#     print("num1 == num2")

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def __detitem__(self, item):
#         if item == "name":
#             return self.__name
#         elif item == "age":
#             return self.__age
        
#         return None
    
# ivan=Person("Ivan", 20)
# print("Name:", ivan["name"])
# print("Age:", ivan["age"])
# print("Nick:", ivan["nick"])

# class Person1:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def __contains__(self, item):
#         if item == "name" or item == "age":
#             return True
#         return False
    
# ivan1=Person1("Ivan", 20)
# print("name" in ivan1)
# print("age" in ivan1)
# print("nick" in ivan1)

# # Задача:
# class Airplane:
#     def __init__(self, model, max_passengers):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = 0
#     def __eq__(self, other):
#         return self.__class__==other.__class__ 
    
#     def __iadd__(self, value):
#         self.current_passengers += value
#         if self.current_passengers > self.max_passengers:
#             print("Невозможно добавить пассажиров")
#             return self

# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#     def __eq__(self, other):
#         return self.area == other.area 
#     def __ne__(self, other):
#         return self.area != other.area
    
#     def __gt__(self, other):
#         return self.price > other.price
    
#     def __lt__(self, other):
#         return self.price < other.price
    
# flat1=Flat(60, 3000000)
# flat2=Flat(45, 2500000)
# flat3=Flat(60, 3500000)
# print(flat1==flat3)
# print(flat1==flat2)
# print(flat1!=flat2)
# print(flat1<flat3)
# print(flat3>flat2)

class GameScoreMathError(Exception):
    pass
class GameScore:
    MIN_SCORE = 0
    MAX_SCORE = 1000
    def __init__(self, score):
        self.score = self._validate_score_limit(score)
    def __str__(self):
        return f"Ваши очки: {self.score}"
    def __repr__(self):
        return f"GameScore(score={self.score}")
    def _validate_other_type(other)
        