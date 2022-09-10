# https://www.beecrowd.com.br/judge/pt/problems/view/1013

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

def maiorAB(numA, numB):
    return int((numA + numB + abs(numA - numB)) / 2)

ab = maiorAB(a, b)
abc = maiorAB(ab, c)

print(f"{abc} eh o maior")