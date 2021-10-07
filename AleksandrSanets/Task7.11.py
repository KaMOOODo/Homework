"""Implement a generator which will generate [Fibonacci numbers] endlessly."""


def endless_fib_generator():
    step = 1
    next_step = 1
    while step > 0:
        yield step
        step, next_step = next_step, step+next_step


gen = endless_fib_generator()
while True:
    print(next(gen))
# >>> 1 1 2 3 5 8 13