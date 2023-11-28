class Users:

    def __init__(self, filepath: str) -> None:
        """Инициализация базы данных.

        Аргументы:
            filepath: Путь к базе данных.
        """

    def create_account(self, name: str, password: str):
        """Создаёт аккаунт.

        Аргументы:
            name: Логин аккаунта.
            password: Пароль от аккаунта.

        Возвращаемое значение: Статус выполнения, id в случае успеха.
        """

    def login_account(self, name: str, password: str):
        """Входит в аккаунт.

        Аргументы:
            name: Логин аккаунта.
            password: Пароль от аккаунта.

        Возвращаемое значение: Статус выполнения, id в случае успеха.
        """

    def find_user(self, username: str):
        """Ищет пользователя по username.

        Аргументы:
            username: Имя пользователя.

        Возвращаемое значение:
            False: Пользователь не найден.
            list[int, str]: ID пользователя и его имя.
        """

    def send_message(self, login: str, receiver: int, message: str) -> bool:
        """Создаёт запись в базе данных о сообщении."""

    def close(self) -> None:
        """Закрывает базу данных."""

class Network:

    def __init__(self, sock: socket, addr) -> None:
        pass

    @staticmethod
    def encode_message(message) -> bytes:
        """Превращает объекты в байты."""

    @staticmethod
    def decode_message(message: bytes):
        """Превращает байты в объекты."""

    def encrypion_message(message: str):
        """Кодиует сообщение message с помощью шифра."""

    def decrypcion_message(message: str):
        """Декодирует сообщение message с помощью ключа шифрования."""

    def send(self, message: list) -> None:
        """Отправляет сообщение клиенту.

        Аргументы:
            message: Сообщение.
        """

    def send_account_data(self) -> None:
        """Отправляет данные об аккаунте."""

    def receive(self, jdata: bytes) -> bool:
        """Получает сообщение от клиента.

        Аргументы:
            jdata: Данные от клиента.

        Возвращаемое значаени: Надо ли обновлять таймер сообщений?
        """

    def close(self) -> None:
        """Закрывает соединение с клиентом."""

    def main() -> None:
        """Основная функция."""