from sqlalchemy import create_engine
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import json

class Users:

    def __init__(self, filepath: str) -> None:
        """Инициализация базы данных.
        Аргументы:
            filepath: Путь к базе данных.
        """
        self.__con = connect(filepath)
        self.__cur = self.__con.cursor()

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

    def send_message(self, login: str, receiver: int, message: str, sender, token) -> bool:
        """Создаёт запись в базе данных о сообщении."""

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "type": "message",
            "From": sender,
            "To": receiver,
            "Text": message
        })

        response = requests.post(
            f"{base_url}/send-message",
            headers=headers,
            data=payload
        )
        if response.status_code != 200:
            print(f"Error: {response.status_code}: {response.text}")
            return

        print(f"Сообщение отправлено!")

Base = declarative_base()

class Messages(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender = Column(Str)
    receiver = Column(Str)
    text = Column(Str)

    """Создает диспетчер сеансов для обработки подключения к базе данных."""

    engine = create_engine('sqlite:///messages.db')
    Session = sessionmaker(bind=engine)

    def persist_message(message: Message):
        """Создаёт сеанс."""
        with Session() as session:
            """Создаёт объект сообщения и добавляет его в базу данных."""

            msg = Messages(sender = message.sender, receiver = message.receiver, text = message.text)
            session.add(msg)
            session.commit()

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