# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

venda1 = input()
venda2 = input()
venda1 = venda1.split(" ")
venda2 = venda2.split(" ")
total = (int(venda1[1]) * float(venda1[2])) + (int(venda2[1]) * float(venda2[2]))
print(f"VALOR A PAGAR: R$ {total:.2f}")