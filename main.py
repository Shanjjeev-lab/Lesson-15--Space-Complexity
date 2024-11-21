def func1(n):
    print(n)
    if n == 0 or n == 1:
        return 1
    return n * func1(n-1)

print(f"factorial is {3} factorial: {3}")

def func2(n):
    if n < 1:
        return 0
    print(n)
    return func2(n-1)
print(func2(5))