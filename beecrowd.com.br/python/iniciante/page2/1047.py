# https://www.beecrowd.com.br/judge/pt/problems/view/1047

h1, m1, h2, m2 = list(map(int, input().split()))

horas = 24 - h1 + h2

minutos = m2 - m1
if m2 < m1:
    horas -= 1
    minutos = 60 - abs(m2 - m1)

if horas > 24:
    horas -= 24

if horas == 24 and minutos > 0:
    horas -= 24

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
