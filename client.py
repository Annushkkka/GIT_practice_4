import socket

def start_client():
    host = 'localhost'  # Хост сервера
    port = 9090  # Порт сервера

    # Создаем сокет
    client_socket = socket.socket()
    client_socket.connect((host, port))  # Подключаемся к серверу
    print("Соединение с сервером установлено.")

    # Вводим сообщение для отправки на сервер
    message = input("Введите сообщение для отправки на сервер: ")

    # Отправляем данные на сервер
    client_socket.send(message.encode())
    print(f"Отправлено серверу: {message}")

    # Получаем ответ от сервера
    data = client_socket.recv(1024)
    print(f"Ответ от сервера: {data.decode()}")

    # Закрываем соединение
    client_socket.close()
    print("Соединение с сервером закрыто.")

if __name__ == "__main__":
    start_client()
