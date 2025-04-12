from abc import ABC, abstractmethod

class AbstractNotification(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class EmailNotification(AbstractNotification):
    def notify(self, message: str) -> None:
        print(f'Отправлено уведомление по электронной почте {message}')


class TelegramNotification(AbstractNotification):
    def notify(self, message: str) -> None:
        print(f'Отправлено уведомление в Телеграм {message}')


class Blog:
    def __init__(self) -> None:
        self.subscribers: list[Any] = []

    def subscribe(self, subscriber: AbstractNotification) -> None:
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: AbstractNotification) -> None:
        self.subscribers.remove(subscriber)

    def new_post(self, title: str) -> None:
        for subscriber in self.subscribers:
            subscriber.notify(title)


blog = Blog()
email_notification = EmailNotification()
telegram_notification = TelegramNotification()

blog.subscribe(email_notification)
blog.subscribe(telegram_notification)

blog.new_post('Новая статья')

blog.unsubscribe(email_notification)

blog.new_post('Новая статья')



