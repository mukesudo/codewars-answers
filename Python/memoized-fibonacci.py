fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n > 1:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = value
    return value