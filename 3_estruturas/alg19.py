dia_semana = int(input('Digite um número de 1 a 7 para representar o dia da semana:'))
if dia_semana == 1:
    print('Domingo')
elif dia_semana ==2:
    print("Segunda-Feira")
elif dia_semana == 3:
    print("Terça-feira")
elif dia_semana == 4:
    print("Quarta-feira")
elif dia_semana == 5:
    print("Quinta-feira") 
elif dia_semana == 6:
    print("Sexta-feira")       
elif dia_semana==7:
    print("Sabado")
else:
    print("Dia da semana inválido")

    # OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Encadeamento de Condições):
# 
# 1. Resolução do Problema 1:
#    - Este código corrige com sucesso a lógica que havia falhado no arquivo 'problema1.py'.
#    - Agora, o input foi salvo em uma variável ('dia_semana') e convertido para 'int' corretamente.
# 
# 2. Encadeamento Longo com 'elif':
#    - O 'elif' é ideal para cenários com muitas opções exclusivas (como os 7 dias da semana).
#    - O Python testa uma por uma, de cima para baixo. Assim que encontra a verdadeira, executa o bloco e pula o restante.
# 
# 3. Validação com o 'else' (Linha 16):
#    - Funciona como uma rede de segurança para tratar erros de digitação.
#    - Se o usuário digitar qualquer número fora do intervalo de 1 a 7 (ex: 0, 9 ou -5), cai direto no "Dia da semana inválido".
