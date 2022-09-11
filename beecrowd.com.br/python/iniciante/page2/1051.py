# https://www.beecrowd.com.br/judge/pt/problems/view/1051

valor = float(input())


def calc_imposto(val):
    vl8, vl18, vl28 = 0, 0, 0

    if val > 2000:
        val -= 2000
    else:
        val = 0
    
    if val > 1000:
        vl8 = 80.0
        val -= 1000
    else:
        vl8 = val * 0.08
        val = 0

    if val > 1500:
        vl18 = 270.0
        val -= 1500
    else:
        vl18 = val * 0.18
        val = 0
    
    if val > 0:
        vl28 = val * 0.28
    
    result = vl8 + vl18 + vl28

    if result > 0:
        return f'R$ {result:.2f}'
    return "Isento"


print(calc_imposto(valor))
