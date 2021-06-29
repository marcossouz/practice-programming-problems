# https://projecteuler.net/problem=4

largest_palindrome = 0
for i in range(999, 99, -1):
    for ii in range(999, i, -1):
        prod = i * ii
        reverse = str(prod)[::-1]
        if str(prod) == reverse:
            if prod > largest_palindrome:
                largest_palindrome = prod

print(largest_palindrome)
