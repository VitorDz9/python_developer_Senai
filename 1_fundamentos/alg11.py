
nota1=int(input("Digite sua nota 1:"))
nota2=int(input("Digite sua nota 2:"))
nota3=int(input("Digite sua nota 3:"))

soma = nota1+nota2+nota3
media= soma/3

print(f"Sua nota media foi {media}")

if media >=6:
    print(f"Você foi aprovado com {media} de nota")

else:
    print(f"Você não foi aprovado, sua media foi {media}")

    # OBSERVAÇÕES IMPORTANTES SOBRE O CÓDIGO (Cálculo de Média e Condicionais):
# 
# 1. Entrada de Múltiplos Dados (Linhas 1 a 3):
#    - Coleta três notas consecutivas e converte todas para inteiro ('int').
#    - Se o usuário digitar uma nota com ponto decimal (ex: 7.5), o 'int()' dará erro. Para aceitar decimais, o ideal seria usar 'float()'.
# 
# 2. Operadores Aritméticos (Linhas 5 e 6):
#    - Realiza a soma das variáveis e depois a divisão por 3.
#    - Em Python, o operador '/' sempre retorna um número decimal (float), mesmo que o resultado seja exato.
# 
# 3. Operador de Comparação (Linha 10):
#    - Usa o operador '>=' (maior ou igual) para definir o critério de aprovação (nota 6).
