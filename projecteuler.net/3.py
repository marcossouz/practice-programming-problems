# https://projecteuler.net/problem=3


def prime_factors(n):
    products = 1
    for i in range(3, n):
        if n % i == 0:
            products *= i
            print(i)
        if products == n:
            break


if __name__ == '__main__':
    N = int(input())

    # N = '600851475143'
    # largest prime factor: 6857
    prime_factors(N)
