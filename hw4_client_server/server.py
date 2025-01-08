import socket


def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Сервер запущено на {host}:{port}. Очікування клієнтів...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Зʼєднання встановлено з {client_address}")

        message = client_socket.recv(1024).decode('utf-8')
        print(f"Повідомлення від клієнта: {message}")

        response = "Повідомлення отримано!"
        client_socket.send(response.encode('utf-8'))

        client_socket.close()
        print(f"Зʼєднання з {client_address} закрито")


if __name__ == "__main__":
    start_server()
