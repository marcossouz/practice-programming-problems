# https://www.beecrowd.com.br/judge/pt/problems/view/1012

PI = 3.14159
entrada = input()
values = entrada.split(' ')
A, B, C = float(values[0]), float(values[1]), float(values[2])

triangulo = (A * C) / 2
circulo = PI * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")