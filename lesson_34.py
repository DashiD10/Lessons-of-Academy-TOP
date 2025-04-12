from abc import ABC, abstractmethod

class AbstractState(ABC):
    @abstractmethod
    def press_play(self):
        pass

    @abstractmethod
    def press_pause(self):
        pass

    @abstractmethod
    def press_stop(self):
        pass


class PlayingState(AbstractState):
    def __init__(self, player):
        self.player = player

    def press_play(self):
        print('Музыка уже играет')

    def press_pause(self):
        print('Пауза')
        self.player.set_state(PausedState(self.player))

    def press_stop(self):
            print('Стоп')
            self.player.set_state(StoppedState(self.player))


class PausedState(AbstractState):
    def __init__(self, player):
        self.player = player

    def press_play(self):
            print('Продолжение воспроизведения')
            self.player.set_state(PlayingState(self.player))

    def press_pause(self):
        print('Музыка уже на паузе')

    def press_stop(self):
            print('Стоп')
            self.player.set_state(StoppedState(self.player))


class StoppedState(AbstractState):
    def __init__(self, player):
        self.player = player

    def press_play(self):
        print('Воспроизведение начато')
        self.player.set_state(PlayingState(self.player))

    def press_pause(self):
            print('Музыка остановлена. Невозможно поставить на паузу')

    def press_stop(self):
                print('Музыка остановлена')


class MusicPlayer:
    def __init__(self):
        self.state = StoppedState(self)

    def set_state(self, state: AbstractState):
        self.state = state

    def press_play(self):
            self.state.press_play()

    def press_pause(self):
            self.state.press_pause()

    def press_stop(self):
            self.state.press_stop()

if __name__ == '__main__':
    player = MusicPlayer()

    player.press_play()
    player.press_pause()
    player.press_play()
    player.press_stop()
    player.press_pause()
    player.press_stop()
    player.press_play()
    