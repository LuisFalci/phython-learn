nome_paciente = str(input("Qual o nome do paciente? "))
peso_paciente = float(input(f"Qual o peso do paciente? "))
altura_paciente = float(input(f"Qual a altura do paciente? "))
idade_paciente = int(input(f"Qual a idade do paciente? "))

imc = peso_paciente / (altura_paciente ** 2)
# python aceita encadear comparações (sem necessidade do and)
if imc < 18.5:
    print("Classificação: Baixo peso")
# elif imc >= 18.5 and imc <= 24.9 :
elif 18.5  <= imc <= 24.9 :
    print("Classificação: Peso normal")
elif 25 <= imc <= 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

