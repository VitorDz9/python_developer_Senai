mercados= ['ações','opções','futuro','dolar','ouro','criptomoedas']


print(mercados)
                        #vc usa a variavel [] pra lista uma sequencia de coisas
print(mercados[0:2]) #vc consegue colocar o : para so seguir alguma coisa
print("Senai" in mercados) # O in ele pecorre toda a lista procurando alguma coisa

# OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Fatiamento de Listas e Operador 'in'):
# 
# 1. Fatiamento de Listas / Slicing (Linha 6):
#    - O operador ':' permite extrair uma sublista ou pedaço da lista original.
#    - O formato '[0:2]' pega do índice 0 até o índice anterior ao 2 (ou seja, posições 0 e 1).
#    - O índice final é EXCLUSIVO, por isso ele traz apenas os dois primeiros itens ('ações' e 'opções').
# 
# 2. Operador de Pertencimento 'in' (Linha 7):
#    - O 'in' serve para verificar se um elemento exato existe dentro da lista, retornando True (Verdadeiro) ou False (Falso).
#    - Ele diferencia maiúsculas de minúsculas e caracteres especiais (acentos).
# 
# 3. Correção de Erro (Linha 7):
#    - O print retornou 'False' no terminal porque foi digitado "Senal" com "S" maiúsculo e sem o til (~).
#    - Para encontrar o elemento da lista, deveria ser escrito "ações" exatamente igual à criação da lista.
