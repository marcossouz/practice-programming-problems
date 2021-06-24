# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

A, B = list(map(int, input().split()))

if A % B == 0 or B % A == 0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
