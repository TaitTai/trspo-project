import socket
import struct
from concurrent.futures import ThreadPoolExecutor

def matrix_multiply(A, B):
    """Функція для множення двох матриць A і B"""
    n, m = len(A), len(A[0])
    m2, l = len(B), len(B[0])
    if m != m2:
        raise ValueError("Матриці не можна перемножити: кількість стовпців A не дорівнює кількості рядків B.")

    result = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result

def handle_client(conn, addr):
    """Обробка клієнтського запиту"""
    try:
        n, m = struct.unpack('ii', conn.recv(8))
        matrix_A = []
        for _ in range(n):
            row = struct.unpack(f'{m}i', conn.recv(m * 4))
            matrix_A.append(list(row))

        m2, l = struct.unpack('ii', conn.recv(8))
        matrix_B = []
        for _ in range(m2):
            row = struct.unpack(f'{l}i', conn.recv(l * 4))
            matrix_B.append(list(row))

        result = matrix_multiply(matrix_A, matrix_B)

        conn.send(struct.pack('ii', len(result), len(result[0])))
        for row in result:
            conn.send(struct.pack(f'{len(row)}i', *row))

    except Exception as e:
        print(f"Помилка обробки запиту: {e}")
    finally:
        conn.close()

def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    with ThreadPoolExecutor(max_workers=4) as executor:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((server_ip, server_port))
            s.listen(5)
            print(f"Сервер слухає на {server_ip}:{server_port}...")

            while True:
                conn, addr = s.accept()
                print(f"Підключено до {addr}")

                executor.submit(handle_client, conn, addr)

if __name__ == "__main__":
    main()
