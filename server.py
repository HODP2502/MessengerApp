from functools import singledispatchmethod
from msilib.schema import Property
from typing import Any, Dict
import requests
import json
import sqlite3

class Users:
    username: str
    login: str
    email: str
    password: str

    def create_account(username, password, email):

            conn = sqlite3.connect('mydatabase.db')

            cur = conn.cursor()

            cur.execute("INSERT INTO my_table (username, password, email) Values (?, ?, ?)",
                        (username, password, email))

            conn.commit()

            conn.close()

            if cur.lastrowid is not None:
                return cur.lastrowid
            else:
                return None
        """Создаёт аккаунт.
        Аргументы:
            username: Логин аккаунта.
            password: Пароль от аккаунта.
        Возвращаемое значение: Статус выполнения, id в случае успеха."""

    def login_account(self, username: str, password: str):
        """Входит в аккаунт.
                Аргументы:
                    username: Логин аккаунта.
                    password: Пароль от аккаунта.
                Возвращаемое значение: Статус выполнения, id в случае успеха."""
        conn = sqlite3.connect('mydatabase.db')

        cur = conn.cursor()

        cur.execute("SELECT username, password, FROM my_table WHERE username = ? AND password = ?",
                    (username, password))
        results = cur.fetchone()

        if results is not None and results[0] == username and results[1] == password:
            return True
        else:
            return False

    def search_user(request, user_name):
        conn = sqlite3.connect('messaging.db')
        cur = conn.cursor()

        cur.execute(f"""
                    SELECT id, from, to, subject, body
                    FROM messages
                    WHERE user_name = ?""", (user_name,))

        results = cur.fetchall()

        if results:
            id = results[0][0]
            from = results[0][1]
            to = results[0][2]
            subject = results[0][3]
            body = results[0][4]

            return 'You were not able to find a user with that name.'

        cur.close()
        conn.close()
        """Ищет пользователя по username.
        Аргументы:
            username: Имя пользователя.
        Возвращаемое значение:
            False: Пользователь не найден.
            list[int, str]: ID пользователя и его имя."""

    def send_message(request, user_name, to_name, subject, body):
        conn = sqlite3.connect('messaging.db')
        cur = conn.cursor()

        cur.execute(f"""
                INSERT INTO messages (from, to, subject, body)
                VALUES (?, ?, ?, ?)""", (user_name, to_name, subject, body))

        conn.commit()

        cur.close()
        conn.close()


Base = declarative_base()

class Messages(Base):
        def __init__(self, from, to, subject, body):
            self.
            from = from
            self.to = to
            self.subject = subject
            self.body = body

        def create(self):
            con = sqlite3.connect('messaging.db')
            cur = con.cursor()
            try:
                cur.execute("""CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    from INTEGER NOT NULL,
                    to INTEGER NOT NULL,
                    subject TEXT NOT NULL,
                    body TEXT NOT NULL
                )""")
                cur.execute("""INSERT INTO messages (from, to, subject, body) VALUES (?, ?, ?, ?)""",
                self.from, self.to, self.subject, self.body)
                con.commit()

            except sqlite3.Exception as ex:
                if ex.errno != None:
                    # обработка конкретной ошибки
                    if ex.errno == 1067:
                        # ошибка при вставке данных
                        cur.execute("""INSERT INTO messages (from, to, subject, body)
                        VALUES (?, ?, ?, ?""",
                                    (self.from, self.to, self.subject, self.body)
                                    )
                        con.commit()

                return None
            except Exception as ex:
                # обработка непредвиденных ошибок
                return None

        def read(self):
            con = sqlite3.connect('messaging.db')
            cur = con.cursor()
            cur.execute("""SELECT * FROM messages WHERE id = ?""", self.id)
            return cur.fetchone()

        def update(self):
            con = sqlite3.connect('messaging.db')
            cur = con.cursor()
            cur.execute("""UPDATE messages SET
            from = ?, to = ?, subject = ?, body = ? WHERE
            id = ?""",self.from, self.to, self.subject, self.body)
            con.commit()

        def delete(self):
            con = sqlite3.connect('messaging.db')
            cur = con.cursor()
            cur.execute("DELETE FROM messages WHERE id = ?", self.id)
            con.commit()


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