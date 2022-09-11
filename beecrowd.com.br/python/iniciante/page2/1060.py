# https://www.beecrowd.com.br/judge/pt/problems/view/1060


inputs = [input(), input(), input(), input(), input(), input()]
values = map(lambda i: float(i), inputs)

qt_positivos = [i for i in values if i > 0]

print(f"{len(qt_positivos)} valores positivos")
