def fibonacci_loop(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    
    while len(series) < n:
        next_num = series[-1] + series[-2]
        series.append(next_num)
        
    return series

print(fibonacci_loop(10))
