import socket
import struct

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Підключено до сервера {host}:{port}")

    try:
        for i in range(100):  # Надсилаємо 100 повідомлень
            message = f"Повідомлення {i + 1}"
            message_bytes = message.encode('utf-8')

            client_socket.sendall(struct.pack('!I', len(message_bytes)) + message_bytes)

            header = client_socket.recv(4)
            if not header:
                break

            response_length = struct.unpack('!I', header)[0]

            response = client_socket.recv(response_length).decode('utf-8')
            print(f"Відповідь від сервера: {response}")

    finally:
        client_socket.close()
        print("Клієнт завершив роботу")

if __name__ == "__main__":
    start_client()
