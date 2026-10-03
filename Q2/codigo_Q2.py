def obterNivel(velocidade):
    if velocidade < 10:
        return 1
    elif velocidade >= 10 or velocidade < 20:
        return 2
    else:
        return 3

def mediaNiveis(niveis):
    media = 0
    for nivel in niveis:
        media = media + nivel
    return media / len(niveis)

def maiorNivel(niveis):
    maior = 0
    for i in range(len(niveis[1:])):
        if niveis[i] > niveis[maior]:
            maior = i
    return maior

def menorNivel(niveis):
    menor = 0
    for i in range(len(niveis[1:])):
        if niveis[i] < niveis[menor]:
            menor = i
    return menor

# Ler a entrada
arquivo = open("lesmas.txt", "r")

# Armazena as saidas futuras
saidas = []

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
        saidas.append([ media, maior, menor ])

# Imprime a saida
for i in range(len(saidas)):
    print(f"{saidas[i][0]:.2f} {saidas[i][1]} {saidas[i][2]}")
