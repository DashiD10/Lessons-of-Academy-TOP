from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Post:
    title: str
    content: str
    hashtags: list = field(default_factory=list)
    history: list = field(default_factory=list)

    def __post_init__(self):
        self.add_history(f"Пост '{id(self)}' создан")
    
    def add_history(self, state: str) -> None:
        self.history.append(state)


class AbstractPostHandler(ABC):

    @abstractmethod
    def handle(self, post: Post) -> None:
        pass

class TitleHandlerA(AbstractPostHandler):
    def handle(self, post: Post) -> None:
        result: str = f"Заголовок поста: {post.title}ю Обработчик А"
        print(result)
        post.add_history(result)

class TitleHandlerB(AbstractPostHandler):
    def handle(self, post: Post) -> None:
        result: str = f"Заголовок поста: {post.title}ю Обработчик Б"
        print(result)
        post.add_history(result)

class ContentHandlerA(AbstractPostHandler):
    def handle(self, post: Post) -> None:
        result: str = f"Содержание поста: {post.content}ю Обработчик А"
        print(result)
        post.add_history(result)
        post.content = result


class ContentHandlerB(AbstractPostHandler):
    def handle(self, post: Post) -> None:
        result: str = f"Содержание поста: {post.content}ю Обработчик Б"
        print(result)
        post.add_history(result)
        post.content = result


class BlogProcessor:
    def __init__(self):
        self.title_handlers = {
            "A": TitleHandlerA(),
            "B": TitleHandlerB(),
        }

    def process_post_interactive(self, post: Post) -> Post:
        print("Выберите обработчик заголовка:")
        for key in self.title_handlers.keys():
            print(f"- {key}")

        title_choice = input("Выберите обработчик заголовка или нажмите энтэр для пропуска")

        print("Доступные обработчики контента")
        for key in self.title_handlers.keys():
            print(f"- {key}")

        content_choice = input("Выберите обработчик контента или нажмите энтэр для пропуска")

        if title_choice and title_choice in self.title_handlers:
            post.add_history(f"Выбран обработчик заголовка: {title_choice}")
            self.title_handlers[title_choice].handle(post)

        if content_choice and content_choice in self.title_handlers:
            post.add_history(f"Выбран обработчик контента: {content_choice}")
            self.title_handlers[content_choice].handle(post)

        post.add_history("Пост обработан")
        return post
    
    def process_post(self, post: Post, title_handler_key: str = None, content_handler_key: str = None) -> Post:
        if title_handler_key and title_handler_key in self.title_handlers:
            post.add_history(f"Выбран обработчик заголовка: {title_handler_key}")
            self.title_handlers[title_handler_key].handle(post)

        if content_handler_key and content_handler_key in self.content_handlers:
            post.add_history(f"Выбран обработчик контента: {content_handler_key}")
            self.content_handlers[content_handler_key].handle(post)

        post.add_history("Пост обработан")
        return post
    
def main():

    processor = BlogProcessor()
    post = Post(title="Заголовок поста", content="Содержание поста")

    processed_post = processor.process_post_interactive(post)

    print("\nРезультат")
    print(f"Заголовок: {processed_post.title}")
    print(f"Содержание: {processed_post.content}")
    print("\nИстория изменений")
    for entry in processed_post.history:
        print(entry)


if __name__ == "__main__":
    main()

