# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048


salary = float(input())

percentage_increase = 0
new_salary = 0
if 0 <= salary <= 400:
    percentage_increase = 1.15
elif 400 < salary <= 800:
    percentage_increase = 1.12
elif 800 < salary <= 1200:
    percentage_increase = 1.10
elif 1200 < salary <= 2000:
    percentage_increase = 1.07
elif salary > 2000:
    percentage_increase = 1.04

new_salary = salary * percentage_increase
difference = abs(new_salary - salary)

percentage_format = (percentage_increase - 1) * 100
print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {difference:.2f}")
print(f"Em percentual: {percentage_format:.0f} %")
