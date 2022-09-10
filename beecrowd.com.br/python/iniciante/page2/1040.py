# https://www.beecrowd.com.br/judge/pt/problems/view/1040

N1, N2, N3, N4 = input().split()
N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + N4) / 10

print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media < 7.0:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame}")
    resultado = (nota_exame + media) / 2
    if resultado >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {resultado:.1f}")
