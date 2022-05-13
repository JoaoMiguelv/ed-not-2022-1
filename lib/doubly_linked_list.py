'''
    Classe que representa uma unidade de informação na lista duplamente encadeada.
'''

from numpy import insert


class Node:

    ''' Método construtor '''
    def __init__(self, data):
        self.prev = None    # ponteiro para nodo anterior
        self.data = data    # Dado do usuário
        self.next = None    # ponteiro para nodo seguinte

######################################################################

'''
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos (nodos)
    não estão adjacentes fisicamente uns dos outros, mas ligados
    logicamente por meio de ponteiros que indicam o anterior e
    o próximo nodo da sequência. Não tem restrição de acessos - 
    inserções, exclusões e consultas podem ser realizadas em
    qualquer posição da lista
'''

class DoublyLinkedList:

    ''' 'Método construtor '''
    def __init__(self):
        self.__head = None # Aponta para o primeiro nodo da lista
        self.__tail = None # Aponta para o último nodo da lista
        self.__count = 0    # Mantém o número de nodos da lista

    '''
        Propriedade que retorna a quantidade de itens da lista
    '''
    @property
    def count(self):
        return self.__count
    
    '''
        Propriedade que retorna se a lista está ou não vazia 
    '''
    @property
    def is_empty(self):
        return self.__count == 0

    '''
        Método que insere um valor na posição especificada
    '''
    def insert(self, pos, val):
        # Criamos um nodo que contém a informação do usuário e também
        # os ponteiros prev e next apontando para o None
        inserted = Node(val)

        # 1° Caso: Lista vazia e este é o primeiro nodo a ser inserido
        if self.is_empty:
            self.__head = inserted
            self.__tail = inserted
        
        # 2° Caso: Inserção na posição inicial (posição)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted

        # 3° Caso: Inserção na posição final (qualquer posição >= count)
        elif pos >= self.count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # 4° Caso: Inserção na posição intermediária (entre os nodos)
        else:
            # Encontrar o nodo atualmente na posição de inserção
            node_pos = self.__find_node(pos)
            # Encontra o nodo da posição anterior à de inserção
            before = node_pos.prev


        # Incrementa a contagem de itens
        self.__count += 1
    
    '''
       Função privada que encontra o nodo da posição especificada
    '''
    def __find_node(self, pos):
        # 1° Caso: Posição 0, retorna __head
        if pos == 0:
            return self.__head

        # 2° Caso: Posição = count-1, retorna __tail
        elif pos == self.count-1:
            return self.__tail
        
        # 3° Caso: nodo intermediário, retorna o nodo da posição
        else:
            # Se o nodo estiver na primeira metade da lista,
            # faz o percurso a partir de __head, seguindo o next
            if pos <= self.count//2:
                node = self.__head
                for i in range(1, pos + 1):
                    node = node.next

            # Senão, faz o percurso a partir de __tail, seguindo o prev
            else:
                node = self.__tail
                for i in range(self.count - 2, pos - 1, -1):
                    node = node.prev

            return node
