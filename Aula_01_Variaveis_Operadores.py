nome_paciente = str(input("Qual o nome do paciente?"))
idade_paciente = int(input("Qual a idade do paciente?"))
altura_paciente = float(input("Qual a altura do paciente?"))
peso_paciente = float(input("Qual o peso do paciente?"))

imc = peso_paciente / (altura_paciente ** 2)

print(f"O paciente {nome_paciente}, de {idade_paciente} anos, possui um imc de {imc:.2f}")