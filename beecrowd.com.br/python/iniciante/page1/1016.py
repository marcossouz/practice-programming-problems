# https://www.beecrowd.com.br/judge/pt/problems/view/1016

km = int(input())
carro1 = 1
carro2 = 1.5

while abs(carro2 - carro1) < km:
    carro1 += 1
    carro2 += 1.5

print(f"{carro1} minutos")