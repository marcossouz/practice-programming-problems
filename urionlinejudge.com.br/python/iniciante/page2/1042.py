# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

values = list(map(int, input().split()))

original = values.copy()
values.sort()

for i in values:
    print(i)

print('')
for i in original:
    print(i)
