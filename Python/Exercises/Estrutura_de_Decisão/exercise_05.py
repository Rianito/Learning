'''
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

average = 0 
for i in range(2):
    while True:
        try:
            sum += float(input(f"Digite a {i+1}a nota: "))
            break
        except ValueError:
            print("Digite um numero valido.")
average /= 2
message = ""
if average >= 10:
    message = "Aprovado com Dinstincao"
elif average >= 7:
    message = "Aprovado"
else:
    message = "Reprovado"

print(f"{message}\nMedia: {average}")