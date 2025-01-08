import socket
import random
import struct

def generate_matrix(n, m):
    """Генерація випадкової матриці розміру n x m"""
    return [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]

def send_matrix_data(matrix, conn):
    """Відправка розміру та елементів матриці до сервера"""
    n, m = len(matrix), len(matrix[0])
    conn.send(struct.pack('ii', n, m))  # Відправка розміру матриці
    for row in matrix:
        conn.send(struct.pack(f'{m}i', *row))  # Відправка елементів кожного рядка

def receive_result(conn):
    """Отримання результату від сервера"""
    n, m = struct.unpack('ii', conn.recv(8))  # Розмір результату
    result = []
    for _ in range(n):
        result.append(list(struct.unpack(f'{m}i', conn.recv(m * 4))))
    return result

def main():
    N, M, L = random.randint(1000, 2000), random.randint(1000, 2000), random.randint(1000, 2000)
    matrix_A = generate_matrix(N, M)
    matrix_B = generate_matrix(M, L)

    print(f"Розміри матриць: A({N}x{M}), B({M}x{L})")

    server_ip = '127.0.0.1'
    server_port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))

        send_matrix_data(matrix_A, s)
        send_matrix_data(matrix_B, s)

        result = receive_result(s)

        print("Результат обчислення:")
        for row in result:
            print(row)

if __name__ == "__main__":
    main()
