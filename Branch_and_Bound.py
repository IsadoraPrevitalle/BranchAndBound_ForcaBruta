#Essa biblioteca fornece funções para criar e manipular iteradores de forma eficiente.
import itertools

def branchAndBound(Tarefa):
    # verificando o tamanho da matriz (objeto iteravel)
    NumTarefas = len(Tarefa)

    # Gera todas as permutações possíveis da matriz e as tranformam em uma lista
    permutations = list(itertools.permutations(range(NumTarefas)))

    print("Ordens de tarefas posiveis: ",permutations)
    print("Ordem de tarefas atuais: ",Tarefa)

    # Inicializa o valor da melhor solução e a melhor ordem de tarefas
    Melhor_sol = float("inf") #declarando que a variavel será o menor valor possivel
    contador = None #variavel vazia ou não inicializada

    # Para cada permutação de tarefas, calcula o custo total
    for ordem in permutations:
        Custo_atual = 0

        # Verifica se o custo parcial já excede o custo da melhor solução encontrada até agora
        if Custo_atual >= Melhor_sol:
            continue

        # Calcula o custo total da permutação atual - o calculo é realizado pela soma dos elementos q estão em cada posição da matriz
        for i in range(NumTarefas):
            Custo_atual += Tarefa[ordem[i]][i]

            # Verifica se o custo parcial já excede o custo da melhor solução encontrada até agora
            if Custo_atual >= Melhor_sol:
                break

        # Atualiza a melhor solução encontrada, se necessário
        if Custo_atual < Melhor_sol:
            Melhor_sol = Custo_atual
            contador = ordem
        print("Custos: ",Custo_atual)
    return contador, Melhor_sol


# Exemplo de uso:
Tarefa = [
    [2, 3, 1],
    [5, 4, 8],
    [7, 6, 9]
]

contador, Melhor_sol = branchAndBound(Tarefa)

print("Melhor ordem de tarefas:", contador)

print("Custo da melhor solução:", Melhor_sol)



























