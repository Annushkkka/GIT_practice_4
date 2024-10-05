import socket

def start_server():
    host = ''  # Сервер будет доступен для всех интерфейсов
    port = 9090  # Используем порт 9090

    # Создаем сокет
    server_socket = socket.socket()
    server_socket.bind((host, port))  # Привязываем сокет к хосту и порту
    server_socket.listen(1)  # Начинаем прослушивание (макс. 1 клиент в очереди)

    print("Сервер запущен. Ожидание подключений...")
    
    # Принимаем соединение
    conn, addr = server_socket.accept()
    print(f"Клиент подключен: {addr}")

    while True:
        # Принимаем данные от клиента
        data = conn.recv(1024)  # Получаем 1 КБ данных
        if not data:
            break  # Если данных нет, разрываем цикл

        print(f"Получено от клиента: {data.decode()}")
        conn.send(data)  # Отправляем данные обратно клиенту
        print("Данные отправлены клиенту (эхо).")

    # Закрываем соединение
    conn.close()
    print(f"Клиент {addr} отключен.")
    
    # Остановка сервера
    server_socket.close()
    print("Сервер остановлен.")

if __name__ == "__main__":
    start_server()
