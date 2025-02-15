class AdPost:
    promote_rate: float = 0.5

    def __init__(self, title: str, text: str, price: int):
        self.title = title
        self.text = text
        self.price = price
        # self.promote_rate: float = 0.5

    def __str__(self) -> str:
        return f"Заголовок: {self.title}, Текст: {self.text[20]}, Цена: {self.price}"

    def calculate_promote_cost(self, day: int) -> int:
        promote_cost = int(self.price * (self.promote_rate / 100) * day)
        return promote_cost

    @staticmethod
    def get_peak_hours() -> tuple:
        return 13, 14, 15


ap1 = AdPost("Продам ноутбук", "Продам ноутбук в отличном состоянии", 10000)
ap2 = AdPost("Куплю ноутбук", "Куплю ноутбук в отличном состоянии", 10000)

AdPost.promote_rate = 1

print(ap1)
print(ap2)
print(ap1.calculate_promote_cost(10))
print(ap2.calculate_promote_cost(10))
print(AdPost.get_peak_hours())
