def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,100):
    print("The ", i, " fibonacci number is: ", fibonacci(i))