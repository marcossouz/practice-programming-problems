# O Maior

# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

# MaiorAB = (a + b + abs(a - b)) / 2
# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

# Exemplos de Entrada	Exemplos de Saída
# 7 14 106
# 106 eh o maior

# 217 14 6
# 217 eh o maior

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

def maiorAB(numA, numB):
    return int((numA + numB + abs(numA - numB)) / 2)

ab = maiorAB(a, b)
abc = maiorAB(ab, c)

print(f"{abc} eh o maior")