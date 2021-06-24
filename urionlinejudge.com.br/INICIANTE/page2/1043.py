# https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

A, B, C = list(map(float, input().split()))


if (abs(B - C) < A < (B + C)) and (abs(A - C) < B < (A + C)) and (abs(A - B) < C < (A + B)):
    perimetro_triangulo = A + B + C
    print(f"Perimetro = {perimetro_triangulo:.1f}")
else:
    area_trapezio = ((A + B) * C) / 2
    print(f"Area = {area_trapezio:.1f}")
