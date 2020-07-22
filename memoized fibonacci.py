mem={}
def fibonacci(n):
    if n in [0, 1]:
        return n
    if n in mem:
        return mem[n]
    mem[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# test.assert_equals(fibonacci(70), 190392490709135)
# test.assert_equals(fibonacci(60), 1548008755920)
# test.assert_equals(fibonacci(50), 12586269025)