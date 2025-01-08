"""
Результат:
    - час виконання 75.98 сек
    - середня градин 155.27
"""

import threading
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


def _process_range(start, end, results, index):
    results[index] = sum(collatz_steps(num) for num in range(start, end))


def main():
    start_time = time.time()
    n_numbers = 10_000_000
    n_threads = 8

    chunk_size = n_numbers // n_threads
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size + 1) for i in range(n_threads)]

    results = [0] * n_threads
    threads = []

    for i, (start, end) in enumerate(ranges):
        thread = threading.Thread(target=_process_range, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_steps = sum(results)
    average_steps = total_steps / n_numbers if n_numbers else 0

    end_time = time.time()
    print(f"Час виконання: {end_time - start_time:.2f} секунд")
    print(f"Середня кількість кроків: {average_steps}")


if __name__ == "__main__":
    main()
