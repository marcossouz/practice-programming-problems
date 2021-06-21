# https://projecteuler.net/problem=1

sum_of_all = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_all += i

# 233168
print(sum_of_all)
