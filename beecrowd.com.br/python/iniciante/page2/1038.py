# https://www.beecrowd.com.br/judge/pt/problems/view/1038

produtos = {
    '1': {"produto": "Cachorro Quente", "valor": 4.00},
    '2': {"produto": "X-Salada", "valor": 4.50},
    '3': {"produto": "X-Bacon", "valor": 5.00},
    '4': {"produto": "Torrada simples", "valor": 2.00},
    '5': {"produto": "Refrigerante", "valor": 1.50}
}

cod, qt = input().split()
qt = int(qt)

total = qt * produtos[cod]["valor"]
print(f"Total: R$ {total:.2f}")
