# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

days = int(input())

months = 0
years = 0

while days >= 30:
    months += 1
    days -= 30

    if months >= 12:
        years += 1
        months -= 12

        # adjust as indicated in the description
        days -= 5

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
