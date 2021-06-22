# https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

A, B = list(map(float, input().split()))

if A == 0 and B == 0:
    print("Origem")
elif B == 0:
    print("Eixo X")
elif A == 0:
    print("Eixo Y")
elif A > 0 < B:  # + +
    print("Q1")
elif A < 0 < B:  # - +
    print("Q2")
elif A < 0 > B:  # - -
    print("Q3")
elif A > 0 > B:  # + -
    print("Q4")
