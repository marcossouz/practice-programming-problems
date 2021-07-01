# https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

A = raw_input()
B = raw_input()
C = raw_input()

if A == 'vertebrado':
    if B == 'ave':
        if C == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if C == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if B == 'inseto':
        if C == 'hematofago':
            print('pulga')
        else:
            print('lagarto')
    else:
        if C == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
