def even_numbers(n):
    if n < 0:
        raise ValueError("n cannot be negative!")
    
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

try:
    for num in even_numbers(10):
        print(num)
except ValueError as e:
    print(e)