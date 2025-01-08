import random
import string
import time

# Math stuff


def _calculate_factorial(n=10):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def _generate_fibonacci(n=20):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def _sum_of_squares(n=100):
    return sum(i**2 for i in range(n))


def _count_primes(limit=10000):
    primes = []
    for num in range(2, limit):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    return len(primes)


# Strings stuff


def _reverse_string(s="Technolohii rozpodil'chykh system ta obchyslen'"):
    return s[::-1]


def _concatenate_strings(times=1000):
    base = "Taya"
    return "".join(base for _ in range(times))


def _generate_random_string(length=50):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


# Arrays stuff


def _sort_random_list(size=1000):
    data = [random.randint(1, 10000) for _ in range(size)]
    return sorted(data)


def _find_max_in_list(size=1000):
    data = [random.randint(1, 10000) for _ in range(size)]
    return max(data)


def _generate_large_list(size=100000):
    return [i for i in range(size)]


# Pseudo-I/O stuff


def _simulated_io_task():
    time.sleep(2)
    return "I/O Task Completed"


def _fake_file_write(data="Hello, world!", iterations=100):
    for _ in range(iterations):
        _ = data * 100
    return "I/O Task Completed"


# Mapping functions
function_mapping = {
    "calculate_factorial": _calculate_factorial,
    "generate_fibonacci": _generate_fibonacci,
    "sum_of_squares": _sum_of_squares,
    "count_primes": _count_primes,
    "reverse_string": _reverse_string,
    "concatenate_strings": _concatenate_strings,
    "generate_random_string": _generate_random_string,
    "sort_random_list": _sort_random_list,
    "find_max_in_list": _find_max_in_list,
    "generate_large_list": _generate_large_list,
    "simulated_io_task": _simulated_io_task,
    "fake_file_write": _fake_file_write,
}


def run_random_task(task_name=random.choice(list(function_mapping.keys()))):
    print(f"Running function: {task_name}")

    result = function_mapping[task_name]()

    print(f"\nResult: {result}")
