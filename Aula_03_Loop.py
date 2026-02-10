string_saida = "saida"
nome_paciente = ""

while nome_paciente != string_saida:
    nome_paciente = str(input("Informe o nome do paciente ou escreva sair para terminar o cálculo: "))
    if nome_paciente.lower() == string_saida:
        continue
    peso_paciente = float(input(f"Qual o peso do paciente? "))
    altura_paciente = float(input(f"Qual a altura do paciente? "))
    idade_paciente = int(input(f"Qual a idade do paciente? "))
    imc = peso_paciente / (altura_paciente ** 2)
    if imc < 18.5:
        print("Classificação: Baixo peso")
    elif 18.5  <= imc <= 24.9 :
        print("Classificação: Peso normal")
    elif 25 <= imc <= 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")
print("Obrigado por utilizar o sistema!")