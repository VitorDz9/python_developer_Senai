numero = int(input("Digite um numero :"))

if numero > 0:
    print("O numero é positivo")
elif numero < 0 : 
    print("O numero é negativo") 
else:
    print("O numero é nulo")

#try exept finally

# OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Estruturas Condicionais Múltiplas e Erros):
# 
# 1. Estrutura Múltipla com 'elif' (Linha 5):
#    - O 'elif' é a abreviação de 'else if'. Ele serve para testar uma nova condição caso o 'if' lá de cima seja falso.
#    - Permite criar caminhos intermediários antes de cair no 'else' final.
# 
# 2. Lógica de Exclusão (Linhas 3, 5 e 7):
#    - Se um número não é maior que 0 e também não é menor que 0, ele só pode ser igual a zero ('nulo').
#    - O 'else' não precisa de condição nenhuma porque pega tudo o que sobrou.
# 
# 3. Tratamento de Exceções (Linha 10):
#    - O comentário cita os blocos de tratamento de erros. A grafia correta em Python é 'try', 'except' (com "c") e 'finally'.
#    - Eles servem para evitar que o programa feche sozinho se o usuário digitar uma letra em vez de número no 'int(input())'.
