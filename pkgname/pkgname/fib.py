
def fib(n):
    """Fibonacci example function"""
    assert n > 0
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
