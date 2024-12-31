import socket
import struct

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Сервер запущено на {host}:{port}. Очікування клієнтів...")
    conn, addr = server_socket.accept()
    print(f"Зʼєднання встановлено з {addr}")

    try:
        for _ in range(100):
            header = conn.recv(4)
            if not header:
                break

            msg_length = struct.unpack('!I', header)[0]

            message = conn.recv(msg_length).decode('utf-8')
            print(f"Отримано повідомлення: {message}")

            response = f"Підтверджено отримання: {message}"
            response_bytes = response.encode('utf-8')

            conn.sendall(struct.pack('!I', len(response_bytes)) + response_bytes)

    finally:
        conn.close()
        server_socket.close()
        print("Сервер завершив роботу")

if __name__ == "__main__":
    start_server()
