# Ler entradas 1
entrada1 = input().split()
N = int(entrada1[0]) # Numero de funcionarios nos caixas
M = int(entrada1[1]) # Numero de clientes

# Ler entradas 2
entrada2 = input().split()
funcionarios = []
for i in range(N):
    funcionarios.append({
        "processamento": int(entrada2[i]),  # Tempo restante para processamento
        "cliente": -1,                      # Indice do cliente sendo processado
        "ocupado": False,                   # Se o funcionario esta ocupado
        "tempo": int(entrada2[i])           # Tempo necessario para cada item
    })

# Ler entradas 3
entrada3 = input().split()
temp = []
for i in range(M):
    temp.append(int(entrada3[i]))
temp.sort()

clientes = []
for i in range(M):
    clientes.append({
        "itens": temp[i],   # Quantidade de itens
        "em andamento": False,  # Se o cliente esta sendo atendido
        "processado": False     # Se o cliente ja teve todos os itens processados
    })

# Processamento
tempo = 0
finalizado = False
while not finalizado:
    for funcionario in funcionarios:
        if not funcionario["ocupado"]: # Busca um cliente que ainda nao foi atendido ( "processado" = False )
            for i in range(len(clientes)):
                if not clientes[i]["em andamento"] and not clientes[i]["processado"]:
                    funcionario["processamento"] = funcionario["tempo"] * clientes[i]["itens"]
                    funcionario["cliente"] = i
                    funcionario["ocupado"] = True
                    clientes[i]["em andamento"] = True
                    break

    for funcionario in funcionarios:
        if funcionario["ocupado"]:
            funcionario["processamento"] = funcionario["processamento"] - 1 # Processa um segundo
            if funcionario["processamento"] < 1:
                clientes[funcionario["cliente"]]["em andamento"] = False
                clientes[funcionario["cliente"]]["processado"] = True
                funcionario["cliente"] = -1
                funcionario["ocupado"] = False

    atendidos = 0
    for cliente in clientes:
        if cliente["processado"]:
            atendidos = atendidos + 1
    if atendidos == M: # Se todos os clientes foram atendidos
        finalizado = True

    tempo = tempo + 1

# Saida
print(tempo) # Tempo, em segundos, necessario para que todos os clientes sejam atendidos
