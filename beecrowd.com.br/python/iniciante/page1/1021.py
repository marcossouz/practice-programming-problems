# https://www.beecrowd.com.br/judge/pt/problems/view/1021

n100, n50, n20, n10, n5, n2 = 0, 0, 0, 0, 0, 0
m100, m050, m025, m010, m005, m001 = 0, 0, 0, 0, 0, 0


def print_line(quantity, label, note_value):
    print(f"{quantity} {label}(s) de R$ {note_value}")


value = float(input())
while value >= 2:
    if value >= 100:
        n100 += 1
        value -= 100
    elif value >= 50:
        n50 += 1
        value -= 50
    elif value >= 20:
        n20 += 1
        value -= 20
    elif value >= 10:
        n10 += 1
        value -= 10
    elif value >= 5:
        n5 += 1
        value -= 5
    elif value >= 2:
        n2 += 1
        value -= 2

print("NOTAS:")
print_line(n100, "nota", '100.00')
print_line(n50, "nota", '50.00')
print_line(n20, "nota", '20.00')
print_line(n10, "nota", '10.00')
print_line(n5, "nota", '5.00')
print_line(n2, "nota", '2.00')

while value > 0:
    value = round(value, 2)
    if value >= 1.00:
        m100 += 1
        value -= 1.00
    elif value >= 0.50:
        m050 += 1
        value -= 0.50
    elif value >= 0.25:
        m025 += 1
        value -= 0.25
    elif value >= 0.10:
        m010 += 1
        value -= 0.10
    elif value >= 0.05:
        m005 += 1
        value -= 0.05
    else:
        m001 += 1
        value -= 0.01

print("MOEDAS:")
print_line(m100, "moeda", '1.00')
print_line(m050, "moeda", '0.50')
print_line(m025, "moeda", '0.25')
print_line(m010, "moeda", '0.10')
print_line(m005, "moeda", '0.05')
print_line(m001, "moeda", '0.01')
