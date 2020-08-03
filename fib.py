def fib(n):
    previous = 0    
    current = 1
    for i in range(n - 1):        
        current_old = current        
        current = previous + current        
        previous = current_old    
    print(current)

# fib(10)

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n - 2) + fib(n - 1)

# fib(10)

import time

print(time.perf_counter())