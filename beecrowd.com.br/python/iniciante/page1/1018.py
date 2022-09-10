# https://www.beecrowd.com.br/judge/pt/problems/view/1018

def printLine(quantity, note_value):
    print(f"{quantity} nota(s) de R$ {note_value}")


value = int(input())
print(value)

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

while value > 0:
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

    elif value >= 1:
        n1 += 1
        value  -= 1

printLine(n100, '100,00')
printLine(n50, '50,00')
printLine(n20, '20,00')
printLine(n10, '10,00')
printLine(n5, '5,00')
printLine(n2, '2,00')
printLine(n1, '1,00')