# https://www.beecrowd.com.br/judge/pt/problems/view/1017

AUTONOMIA = 12
tempo_gasto = int(input())
velocidade_media = int(input())
combustivel_necessario = (tempo_gasto * velocidade_media) / AUTONOMIA
print(f"{combustivel_necessario:.3f}")