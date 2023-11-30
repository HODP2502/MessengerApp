class WindowApp:

    def __init__(self):

    def place(self, id_: str, element) -> None:
        """Размещает объект element.
               Аргументы:
                   id: Уникальный идентификатор элемента.
                   element: Элемент, который необходимо разместить.
        """

    def pack(self, id: str, element) -> None:
        """Размещает объект element.
               Аргументы:
                   id: Уникальный идентификатор элемента.
                   element: Элемент, который необходимо разместить.
        """

    def clear(self) -> None:
        """Очищает все элементы."""

class MessengerClient:

    def __init__(self):

    @staticmethod
    def encode_message(message) -> bytes:
        """Превращает объекты в байты."""

    @staticmethod
    def decode_message(message: bytes):
        """Превращает байты в объекты."""

    def send(self, message: str) -> None:
        """Отправляет сообщение message на сервер.

        Аргументы:
            message: Сообщение.
        """

    def encrypion_message(message: str):
        """Кодиует сообщение message с помощью шифра."""

    def decrypcion_message(message: str):
        """Декодирует сообщение message с помощью ключа шифрования."""

    def send(self, message: str) -> None:
        """Отправляет сообщение message на сервер.
        Аргументы:
            message: Сообщение.
        """

    def send_message(self, message: str) -> None:
        """Отправляет сообщение на сервер.
        Аргументы:
            message: Сообщение.
        """

    def add_user(self, username: str) -> None:
        """Добавляет пользователя по имени.
        Аргументы:
            username: Имя пользователя.
        """

    def receive(self) -> None:
        """Получает сообщения от сервера."""

    def send_idle(self) -> None:
        """Отправляет сообщение серверу о том, что клиент до сих пор открыт."""

    def main(self):
        """Основная функция клиента."""


    def show_error(title: str, message: str) -> None:
        """Показывает ошибку.
        Аргументы:
            title: Заголовок ошибки.
            message: Описание ошибки.
        """