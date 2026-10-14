# teclado 

#input

nome = input("DIgite seu Nome:")
idade = int(input("Digite sua idade:"))
# processador (U.L.A- UNIDADE DE LOGICA E ARITMETICA)
if idade>=18:
 r=(f"O {nome } é maior de idade \n")
 print(r)

else:
 r = (f"O {nome} é menor de idade \n")
 #impressora ou monitor
 print(r)
 print("Programa encerrado com sucesso...")

# OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Entrada de Dados e Condicionais):
# 
# 1. Entrada de Dados (input):
#    - Todo 'input()' recebe o dado como texto (string) por padrão (como na Linha 5).
#    - Para fazer contas ou comparações numéricas, é obrigatório converter para número usando 'int()' (como na Linha 6).
# 
# 2. Estrutura Condicional (if / else):
#    - O 'if' testa se a condição é verdadeira (idade maior ou igual a 18).
#    - O 'else' é o caminho obrigatório caso a condição do 'if' seja falsa.
#    - Lembrar sempre dos dois pontos ':' no final do 'if' e do 'else'.
# 
# 3. Quebra de Linha (\n):
#    - O caractere '\n' dentro da string pula uma linha automaticamente na tela na hora do print.
