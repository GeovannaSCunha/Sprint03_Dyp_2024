#Matriz para armazenar informações dos estudantes
#Cada estudante será representado por uma lista na matriz: [nome, curso, [treinamentos]]
tabela_estudantes = []

def encontrar_estudante(nome):
    """Encontra o índice de um estudante pelo nome na tabela (matriz)."""
    for i, estudante in enumerate(tabela_estudantes):
        if estudante[0] == nome:  #O nome está na coluna 0 de cada linha
            return i
    return None

def cadastrar_estudante(nome, curso):
    """Cadastra um novo estudante na tabela."""
    if encontrar_estudante(nome) is None:
        #Adiciona uma nova linha para o estudante: [nome, curso, [lista de treinamentos]]
        tabela_estudantes.append([nome, curso, []])
        print(f"Estudante {nome} cadastrado com sucesso.")
    else:
        print(f"Estudante {nome} já está cadastrado.")

def registrar_treinamento(nome, coord_motora, habilidade_manual, resposta_sensorial):
    """Registra uma sessão de treinamento de habilidades no sistema de RV."""
    idx = encontrar_estudante(nome)
    if idx is not None:
        sessao = [coord_motora, habilidade_manual, resposta_sensorial]  #Sessão como uma lista
        tabela_estudantes[idx][2].append(sessao)  #Armazena o treinamento na terceira coluna da matriz
        print(f"Treinamento registrado para {nome}.")
    else:
        print(f"Estudante {nome} não encontrado.")

def calcular_pontuacao(sessao):
    """Calcula a pontuação de desempenho do estudante em uma sessão."""
    pontuacao = (sessao[0] * 0.4) + (sessao[1] * 0.4) + (sessao[2] * 0.2)
    return pontuacao

def avaliar_estudante(nome):
    """Avalia o desempenho em todas as sessões de um estudante e imprime as pontuações."""
    idx = encontrar_estudante(nome)
    if idx is not None:
        total_pontuacao = 0
        total_sessoes = len(tabela_estudantes[idx][2])

        print(f"Avaliação de {nome}:")
        for sessao in tabela_estudantes[idx][2]:
            pontuacao = calcular_pontuacao(sessao)
            total_pontuacao += pontuacao
            print(f"Treinamento {tabela_estudantes[idx][2].index(sessao) + 1}: Pontuação = {pontuacao:.2f}")

        if total_sessoes > 0:
            media_pontuacao = total_pontuacao / total_sessoes
            print(f"Média de Pontuação de {nome}: {media_pontuacao:.2f}")
        else:
            print(f"Não há treinamentos registrados para {nome}.")
    else:
        print(f"Estudante {nome} não encontrado.")

# Exemplo de uso das funções
cadastrar_estudante("Ana Silva", "Medicina")
registrar_treinamento("Ana Silva", coord_motora=9.0, habilidade_manual=8.5, resposta_sensorial=9.2)
registrar_treinamento("Ana Silva", coord_motora=8.5, habilidade_manual=9.0, resposta_sensorial=8.8)

avaliar_estudante("Ana Silva")

cadastrar_estudante("Carlos Souza", "Medicina")
registrar_treinamento("Carlos Souza", coord_motora=7.5, habilidade_manual=7.8, resposta_sensorial=8.0)
avaliar_estudante("Carlos Souza")