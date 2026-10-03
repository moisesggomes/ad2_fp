def obterNivel(velocidade):
    if velocidade < 10:
        return 1
    elif velocidade >= 10 and velocidade < 20:
        return 2
    else:
        return 3

def mediaNiveis(niveis):
    soma = 0
    for nivel in niveis:
        soma = soma + nivel
    return soma / len(niveis)

def maiorNivel(niveis):
    maior = 0
    for i in range(1, len(niveis)):
        if niveis[i] > niveis[maior]:
            maior = i
    return niveis[maior]

def menorNivel(niveis):
    menor = 0
    for i in range(1, len(niveis)):
        if niveis[i] < niveis[menor]:
            menor = i
    return niveis[menor]

# Ler a entrada
arquivo = open("lesmas.txt", "r")

terminado = False # checa se o arquivo chegou ao fim
while not terminado:
    linha = arquivo.readline()
    if len(linha) < 1:
        # Se o arquivo acabou, encerra a leitura e o loop
        arquivo.close()
        terminado = True
    else:
        L = int(linha) # Numero de lesmas no grupo
        linha = arquivo.readline()
        velocidades = linha.split()
        niveis = []
        for i in range(L):
            velocidade = int(velocidades[i])
            niveis.append(obterNivel(velocidade))
        media = mediaNiveis(niveis)
        maior = maiorNivel(niveis)
        menor = menorNivel(niveis)

        # Imprime as saidas
        print(f"{media:.2f} {maior} {menor}")
