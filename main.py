from json import dumps
from json import loads
from math import ceil
from math import floor

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
        for child in self.tk_window.winfo_children():
            child.destroy()

        self.elements = {}
        """Очищает все элементы."""

class MessengerClient:

    def __init__(self):

    @staticmethod
    def encode_message(message) -> bytes:
        """Превращает объекты в байты."""
        if self.__key is None and not self.destroyed:
            self._sock.send(b"\x05\x03\xff\x01")
            self.__queued_requests.append(message)
            return None

        return self.__aes.encrypt(dumps(
            message,
            separators=(",", ":"),
            ensure_ascii=False
        ))

    @staticmethod
    def decode_message(message: bytes):
        """Превращает байты в объекты."""
        if self.__key is None:
            self.__key = message.decode("ascii")
            self.__aes = acrypt(KEY_EXTRA + self.__key)

            for req in self.__queued_requests:
                self.send(req)

            return False

        return loads(self.__aes.decrypt(message))

    def send(self, message: str) -> None:
        """Отправляет сообщение message на сервер.

        Аргументы:
            message: Сообщение.
        """
        msg = self.__encode_message(message)

        if msg is not None:
            self._sock.send(msg)

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
        if self._userid_selected == -1:
            return

        message = message[:65535]

        self.win.messages_input.delete(0, tk.END)
        self.__temp_messages.append([message, self._userid_selected])

        listbox = self.win.userlist

        if self._userid_selected != -1:
            listbox.select_set(
                list(
                    self._logins.keys()
                ).index(str(self._userid_selected))
            )
            self._userid_selected = -1
        else:
            listbox.select_set(0)

        listbox.event_generate("<<ListboxSelect>>")

        self.send(["send_message", message, self._userid_selected])

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