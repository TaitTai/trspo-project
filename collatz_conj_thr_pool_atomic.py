"""
Результат:
    - час виконання 108.74 сек
    - середня градин 155.27
"""

from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import time


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def _process_number(number, total_steps, count, lock):
    steps = collatz_steps(number)
    with lock:
        total_steps[0] += steps
        count[0] += 1


def main():
    start_time = time.time()
    n_numbers = 10_000_000
    n_threads = 8

    total_steps = [0]
    count = [0]
    lock = Lock()

    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        for num in range(1, n_numbers + 1):
            executor.submit(_process_number, num, total_steps, count, lock)

    average_steps = total_steps[0] / count[0] if count[0] else 0

    end_time = time.time()
    print(f"Час виконання: {end_time - start_time:.2f} секунд")
    print(f"Середня кількість кроків: {average_steps}")


if __name__ == "__main__":
    main()
