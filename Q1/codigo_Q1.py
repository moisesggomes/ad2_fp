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
clientes = []
for i in range(M):
    clientes.append({
        "itens": entrada3[i], # Quantidade de itens
        "em andamento": False, # Se o cliente esta sendo atendido
        "processado": False # Se o cliente ja teve todos os itens processados
    })

# Processamento
tempo = 0
while len(clientes) > 0:
    for funcionario in funcionarios:
        if funcionario["ocupado"]:
            funcionario["processamento"] = funcionario["processamento"] - 1
        else:
            funcionario["processamento"] = funcionario["tempo"] # Reseta o contador de tempo de processamento
            for i in range(len(clientes)):
                if not clientes[i]["em andamento"] and not clientes[i]["processado"]:
                    funcionario["cliente"] = i
                    funcionario["ocupado"] = True
                    clientes[i]["em andamento"] = True
                    break
            print()

    tempo = tempo + 1

# Saida
print(tempo) # Tempo, em segundos, necessario para que todos os clientes sejam atendidos
