from abc import ABC, abstractmethod

class AbstractAIRequest(ABC):
    @abstractmethod
    def request(self, prompt: str) -> str:
        pass

class RealAIRequest(AbstractAIRequest):
    def request(self, prompt: str) -> str:
        return f"отправлено запрос к ИИ: {prompt}"
    
class CheckTokens:
    
    max_tokens: int = 200_000

    def check_tokens(self, tokens: int) -> bool:
        if tokens > self.max_tokens:
            print(f'Превышен лимит токенов: {tokens} > {self.max_tokens}')
            return False
        return True
    
class ProxyAIRequest(AbstractAIRequest):
    def __init__(self):
        self.real_request = RealAIRequest()
        self.check_tokens = CheckTokens()

    def request(self, prompt: str) -> str:
        tokens = len(prompt.split())
        if self.check_tokens.check_tokens(tokens):
            print(f'Прокси: количество токенов {tokens} для хапроса {prompt}')
            return self.real_request.request(prompt)
        else:
            return 'Недостаточно токенов'
            

if __name__ == '__main__':
    proxy_request = ProxyAIRequest()
    prompt = 'Как сделать так, чтобы не было прокси?'
    response = proxy_request.request(prompt)
    print(response)
    


