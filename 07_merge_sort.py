# lista = [7, 4, 2, 6, 0, 3, 9, 1, 5, 8]

# # Acha o meio da lista
# meio = len(lista)//2 # // = divisão inteira

# metade1 = lista[:meio] #do início até um antes do meio
# metade2 = lista[meio:] #do meio pra frente

# print(f'Meio: {meio}')
# print(f'Lista: {lista}')
# print(f'Metade 1: {metade1}')
# print(f'Metade 2: {metade2}')

'''
ALGORITMO DE ORDENAÇÃO MERGER SORT

No processo de ordenação, esse algoritmo "desmonta" o vetor original contendo N elementos até obter N vetores de apenas um elemento cada um.
Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor, dessa vez com os elementosjá em ordem
'''
from data.nomes_desord import nomes
from time import time
import tracemalloc

divs = juncoes = comps = 0

def merge_sort(lista):

    global divs, juncoes, comps

    # Só continua se o comprimento da lista for maior que 1
    if len(lista) <=1:
        return lista

    # Encontra a posição do meio da lista
    meio = len(lista)//2

    # Cópia da primeira metade do vetor
    sublista_esq = lista[0:meio]
    # Cópia da segunda metade do vetor
    sublista_dir = lista[meio:]

    divs += 1

    # Chamamos recursivamente a função para que ela continue repartindo cada uma das sublistas em metades
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # AQUI COMEÇA A JUNÇÃO DAS DUAS METADES DA LISTA, ORDENADAMENTE
    pos_esq = pos_dir = 0
    ordenada = [] # Lista vazia

    # Compara os elementos da sublista entre si e insere na lista ordenada o que for menor
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):

        # O elemento que se encontra na posição da sublista esquerda é menor que o que se encontra na posição da sublista direita
        comps += 1
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada. append(sublista_esq[pos_esq])
            pos_esq +=1
        
        # O contrário
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir +=1
    
    # Verificação da sobra
    sobra = []
    
    # Sobra à esquerda
    if pos_esq < pos_dir:
        sobra = sublista_esq[pos_esq:]

    # Sobra à direita
    else:
        sobra = sublista_dir[pos_dir:]

    # O resultado final é a concatenação da lista ordenada com a sobra
    juncoes += 1
    return ordenada + sobra


#####################################################################3


nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = merge_sort(nums) # necessário definir como variável porque deixa o original intacto e cria uma cópia ordenada dele
print(resultado)
print(f'Divisões: {divs}, comparações {comps}, junções: {juncoes}')

divs = juncoes = comps = 0


hora_ini = time()
tracemalloc.start() # Inicia o monitoramento da memória

nomes_ord = merge_sort(nomes)

# Captura as estatísticas do uso da memória
mem_atual, mem_pico = tracemalloc.get_traced_memory() # Função que retorna dois valors (se deixar somente 1 variavel, irá ignorar a segunda resposta da função)
hora_fim = time()

#print(nomes_ord[:100]) # Imprime só os 100 primeiros nomes

print(f'Tempo gasto para ordenar: {(hora_fim - hora_ini)*1000}ms')
print(f'Pico de memória: {mem_pico / 1024 / 1024} MB')
print(f'Divisões: {divs}, comparações {comps}, junções: {juncoes}')