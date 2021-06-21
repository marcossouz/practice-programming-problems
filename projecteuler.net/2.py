# https://projecteuler.net/problem=2

MAX_LIMIT = 4000000


def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_even_terms():
    sum_even = 0
    i = 0
    while True:
        i += 1
        result = fibonacci(i)
        if result > MAX_LIMIT:
            break

        if result % 2 == 0:
            sum_even += result

    # 4613732
    print(sum_even)


if __name__ == '__main__':
    sum_even_terms()
