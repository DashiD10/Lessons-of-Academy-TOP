from abc import ABC, abstractmethod

class YandexPaymentSystem:

    def yandex_payment(self, amount: float) -> str:
        print(f'Оплата {amount} рублей через Яндекс.Деньги')

class RoboKassaPaymentSystem:

    def robo_kassa_payment(self, amount: float, currency: str) -> str:
        return f'Оплата {amount} {currency} через RoboKassa'
    
class AbstractPaymentSystem(ABC):

    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class YandexPaymentSystemAdapter(AbstractPaymentSystem):
    def __init__(self, yandex_payment_system: YandexPaymentSystem) -> None:
        self.yandex_payment_system = yandex_payment_system

    def pay(self, amount: float) -> str:
        return self.yandex_payment_system.yandex_payment(amount)
    
class RoboKassaPaymentSystemAdapter(AbstractPaymentSystem):

    available_currencies = ['RUB', 'USD', 'EUR']
    def __init__(self, robo_kassa_payment_system: RoboKassaPaymentSystem) -> None:
        self.robo_kassa_payment_system = robo_kassa_payment_system

    def __validate_currency(self, currency: str) -> bool:
        return currency in self.available_currencies
    
    def pay(self, amount: float) -> str:
        currency_input = input('Введите валюту: ')

        if not self.__validate_currency(currency_input):
            raise ValueError('Неверная валюта')
        
        return self.robo_kassa_payment_system.robo_kassa_payment(amount, currency_input)
    
class PaymentFacade:

    def  __init__(self) -> None:
        self.yandex_payment_system = YandexPaymentSystem()
        self.robokassa_payment_system = RoboKassaPaymentSystem()
        self.yandex_adapter = YandexPaymentSystemAdapter(self.yandex_payment_system)
        self.robokassa_adapter = RoboKassaPaymentSystemAdapter(self.robokassa_payment_system)

    def pay_with_yandex(self, amount: float) -> str:
        return self.yandex_adapter.pay(amount)
    
    def pay_with_robo_kassa(self, amount: float) -> str:
        return self.robokassa_adapter.pay(amount)
    
    def __call__(self, amount: float, payment_system: str) -> str:
        if payment_system == 'yandex':
            return self.pay_with_yandex(amount)
        elif payment_system == 'robo_kassa':
            return self.pay_with_robo_kassa(amount)
        else:
            raise ValueError('Неверная система оплаты')
        
if __name__ == '__main__':
    payment_facade = PaymentFacade()
    
    try:
        print(payment_facade(1000, 'yandex'))
        print(payment_facade(2000, 'robo_kassa'))
    except ValueError as e:
        print(e)

    


