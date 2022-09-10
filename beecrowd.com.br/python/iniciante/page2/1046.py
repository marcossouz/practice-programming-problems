# https://www.beecrowd.com.br/judge/pt/problems/view/1046

A, B = list(map(int, input().split()))

result = 24 - A + B
if result > 24:
    result -= 24
print(f"O JOGO DUROU {result} HORA(S)")