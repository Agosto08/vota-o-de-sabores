
opcoes = ["Calabresa", "Frango com Catupiry", "Portuguesa", "Mussarela"]

votos = [0, 0, 0, 0]

votos_validos = 0
votos_invalidos = 0

print("=== URNA DE VOTAÇÃO ===")

while True:

    print("\nOpções disponíveis:")

    for i in range(len(opcoes)):
        print(i + 1, "-", opcoes[i])

    print("0 - Encerrar votação")

    voto = int(input("Digite o número da opção desejada: "))

    if voto == 0:
        break

    elif voto >= 1 and voto <= len(opcoes):
        votos[voto - 1] += 1
        votos_validos += 1
        print("Voto registrado com sucesso!")

    else:
        votos_invalidos += 1
        print("Voto inválido!")

print("\n=== RESULTADO DA ENQUETE ===")

for i in range(len(opcoes)):
    print(opcoes[i], "-", votos[i], "votos")

print("\nTotal de votos válidos:", votos_validos)
print("Total de votos inválidos:", votos_invalidos)

maior_voto = votos[0]
indice_vencedor = 0

for i in range(1, len(votos)):
    if votos[i] > maior_voto:
        maior_voto = votos[i]
        indice_vencedor = i

print("\nOpção vencedora:", opcoes[indice_vencedor])
print("Quantidade de votos:", maior_voto)