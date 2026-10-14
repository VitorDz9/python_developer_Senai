'''
Crie um algoritmo que leia dois numeros 
mostre no final qual o número é maior

#-ENTRADA 
#leia um numero 
leia outo numero 

#verificar quem é o maoir 

# mostrar o maior 


'''
print("\nInsira 2 números e eu darei qual dels é maior ")

numero_1 = int(input("Digite o numero 1:"))
numero_2 = int(input("Digite o numero 2 :"))

if numero_1>numero_2:
    print(f"o numero {numero_1} é maior que o {numero_2}")

elif numero_2>numero_1:
    print(f"O numero {numero_2} é maior que o {numero_1}")

else:
    print("Os numeros são iguais")


    # OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Docstrings e Estrutura Condicional Completa):
# 
# 1. Comentários de Múltiplas Linhas / Docstrings (Linhas 1 a 14):
#    - O uso de três aspas simples ('''...''') permite escrever textos longos em várias linhas.
#    - É ideal para documentar o enunciado do problema ou o objetivo do algoritmo.
# 
# 2. Estrutura Condicional Perfeita (if / elif / else):
#    - O código cobre todas as três possibilidades matemáticas possíveis entre dois números:
#      * Primeiro maior que o segundo ('if')
#      * Segundo maior que o primeiro ('elif')
#      * Números exatamente iguais ('else')
# 
# 3. Interpolação Limpa com f-strings (Linhas 21 e 24):
#    - Permite colocar múltiplas variáveis na mesma frase ('{numero_1}' e '{numero_2}') de forma muito legível.