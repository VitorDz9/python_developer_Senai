# desafio- 
'''

 Elabore um programa que leia um numero 
 Verifique se o numero é par ou ímpar 
 e mostre a mensagem na tela 
            "É impar ' ou 'É par "

# entender o problema 
dividir o problema em pedaçinhos pequeninhos 
e ir resolvendo aos poucos 

'''
numero = int(input("Digite um numero:"))

if numero%2==0:            # esse % é a variação analise o resto da divisão 
    print("O Numero é par")

else:
    print("O numero é impar")

# OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Operador de Resto e Lógica Par/Ímpar):
# 
# 1. Resolução de Problemas / Algoritmos (Linhas 9 a 11):
#    - Abordagem correta de "Dividir para Conquistar": quebrar um problema grande em partes menores e resolvê-las passo a passo.
# 
# 2. Operador Módulo '%' (Linha 16):
#    - O símbolo '%' não calcula porcentagem em Python, ele retorna o RESTO de uma divisão inteira.
#    - Exemplo: 5 % 2 resulta em 1 (porque 5 dividido por 2 dá 2, e sobra 1).
# 
# 3. Lógica matemática de Par ou Ímpar (Linha 16):
#    - Todo número par, quando dividido por 2, deixa o resto exatamente igual a 0.
#    - A expressão 'numero % 2 == 0' verifica matematicamente essa regra para tomar a decisão no 'if'.
