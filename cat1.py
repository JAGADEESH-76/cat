def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
n_terms = 10
print("Fibonacci series:", fibonacci(n_terms))
print("hello")
