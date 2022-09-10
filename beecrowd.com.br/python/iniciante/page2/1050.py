# https://www.beecrowd.com.br/judge/pt/problems/view/1050

table_ddd = {
    "61": "Brasilia",
    "71": "Salvador",
    "11": "Sao Paulo",
    "21": "Rio de Janeiro",
    "32": "Juiz de Fora",
    "19": "Campinas",
    "27": "Vitoria",
    "31": "Belo Horizonte"
}

input = input()

print(table_ddd.get(input, 'DDD nao cadastrado'))