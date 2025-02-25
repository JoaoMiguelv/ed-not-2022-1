from lib.stack import Stack

analisador = Stack()

#expr = 'x + (9 - ((y * 2) / 3) + 1)'
#expr = 'x + (9 - ((y * 2) / 3)) + 1)'
expr = '(x + (9 - ((y * 2) / (3) + 1)'

tem_erro = False

# Percorrer a expressão em bsuca de parênteses
for pos in range(len(expr)):
    if expr[pos] == '(':
        analisador.push(pos)

    elif expr[pos] == ')':
        # Se a pilha estiver vazia, temos um erro
        if analisador.is_empty:
            print(f'ERRO: Fecha parêntese da posição {pos} não tem o abre correspondente')
            tem_erro = True

        else:
            # Tira a posição do abre da pilha
            pos_abre = analisador.pop()
            print(f'Abre parêntese da posição {pos_abre} corresponde ao fecha parêntese da posição {pos}')

# Verifica se há sobra na pilha
while not analisador.is_empty:
    pos_abre = analisador.pop()
    print(f'ERRO: Abre parêntese da posição {pos_abre} não tem o fecha correspondente')
    tem_erro = True


if not tem_erro:
    print('*** PARÊNTESES CORRETAMENTE BALANCEADOS ****')