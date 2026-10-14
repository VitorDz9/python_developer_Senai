#---------------ENTRADA----------------
#ler tres notas de um aluno
#ler o nome do aluno 
#ler o numero da turma 
#ler 3 notas
#---------------------PROCESSAMENTO

# Calcular a media 
# verificar status (media >=70 aprovado)
#-----------SAIDA
#Mostrar a soma das notas 
#mostrar a media das notas 
# mostrar se foi aprovado ou nao 
#-----------------------------------

nome = input("DIgite seu nome :")
turma = input("Digite sua turma:")
nota_1= int(input("Digite a nota 1:"))
nota_2 = int(input("Digite a nota 2:"))
nota_3 = int(input("DIgite a nota 3:"))
media = int(nota_1+nota_2+nota_3)/3

if media >= 70:
    print(f"{nome},sua media foi {media}, você esta aprovado! ")


else:
    print(f"{nome}, sua media foi {media}, você foi reprovado")

    # OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Precedência e Formatação):
# 
# 1. Precedência de Operadores Matemáticos (Linha 21):
#    - Em Python, a divisão '/' tem prioridade sobre a soma '+'.
#    - Ao escrever 'nota_1 + nota_2 + nota_3 / 3', o Python vai dividir apenas a 'nota_3' por 3 e depois somar o resto.
#    - Para corrigir e calcular a média certa, a soma DEVE estar entre parênteses: '(nota_1 + nota_2 + nota_3) / 3'.
# 
# 2. Conversão da Média para Inteiro (Linha 21):
#    - O comando 'int(...)' antes da conta remove as casas decimais (ex: 7.6 vira 7).
#    - Se a nota de aprovação for 70, uma média real de 69.8 viraria 69 e o aluno seria reprovado por arredondamento forçado.
# 
# 3. Formatação Interna da f-string (Linhas 24 e 28):
#    - Misturar vírgula com chaves como 'f"{nome}, sua media..."' funciona perfeitamente, pois a vírgula vira um texto comum na tela.
