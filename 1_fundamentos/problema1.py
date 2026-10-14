int(input("Digite um Numero:"))

semana=[1,2,3,4,5,6,7]


if semana == [0,1]:
    print("Segunda Feira ")


    # OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Listas e Entrada de Dados):
# 
# 1. Entrada de Dados sem Armazenamento (Linha 1):
#    - O 'int(input())' está recebendo o número digitado pelo usuário, mas o valor está sendo descartado.
#    - Para usá-lo depois, é obrigatório salvá-lo em uma variável (ex: 'dia = int(input(...))').
# 
# 2. Criação de Listas (Linha 3):
#    - Os colchetes '[]' definem uma estrutura de Lista em Python, que armazena múltiplos valores em sequência.
# 
# 3. Comparação de Tipos Diferentes (Linha 6):
#    - O código tenta comparar a lista inteira ('semana') com outra lista '[0, 1]'.
#    - Para verificar se o número digitado pelo usuário corresponde a um dia da semana, a lógica precisa testar a variável que guardou o input, e não a lista inteira.
