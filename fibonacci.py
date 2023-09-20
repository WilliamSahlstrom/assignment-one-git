def fibonacci(n):
    fib_sequence = [0, 1] 
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence

    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence


n = 10  
fib_numbers = fibonacci(n)
print(fib_numbers)
