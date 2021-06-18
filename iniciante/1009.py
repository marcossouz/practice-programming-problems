# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())
total = salario_fixo + (total_vendas * 0.15)
print(f"TOTAL = R$ {total:.2f}")