dia_semana = int(input("Digite um número de 1 a 7 para representar o dia da semana: "))

match dia_semana:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Dia da semana inválido")

    # OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Estrutura Match-Case):
# 
# 1. Estrutura 'match-case' (Linha 3):
#    - Introduzida no Python 3.10, é o equivalente ao 'switch-case' de outras linguagens.
#    - Substitui perfeitamente longas cadeias de 'if-elif' quando testamos uma única variável.
#    - Deixa o código muito mais limpo, pois não precisamos repetir 'dia_semana ==' em todas as linhas.
# 
# 2. Sintaxe dos Casos (Linhas 4 a 17):
#    - Cada 'case' avalia diretamente o valor literal (1, 2, 3...) contra a variável definida no 'match'.
#    - Assim como no 'if', cada bloco 'case' exige os dois pontos ':' no final.
# 
# 3. O Caso Padrão / Wildcard (Linha 18):
#    - O 'case _:' (com underline) funciona exatamente como o 'else'.
#    - Ele captura qualquer valor que não tenha entrado em nenhum dos casos anteriores (uma rede de segurança).
