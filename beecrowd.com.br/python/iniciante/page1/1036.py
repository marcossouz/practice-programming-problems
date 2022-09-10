# https://www.beecrowd.com.br/judge/pt/problems/view/1036

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)


delta = (B ** 2) - (4 * A * C)

try:
    if delta >= 0:
        x1 = (-B + (delta ** 0.5)) / (2 * A)
        x2 = (-B - (delta ** 0.5)) / (2 * A)
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")
    else:
        print("Impossivel calcular")
except ZeroDivisionError:
    print("Impossivel calcular")
