import socket

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Підключено до сервера {host}:{port}")

        message = "Привіт, сервер!"
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Відповідь від сервера: {response}")

    except ConnectionRefusedError:
        print("Неможливо підключитися до сервера.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
