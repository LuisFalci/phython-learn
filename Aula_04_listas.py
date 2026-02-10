historico_pacientes = []
string_sair = ""
i = 0

while string_sair != "sair":
    nome_paciente = str(input("Informe seu nome ou digite sair para encerrar o fluxo: "))
    if nome_paciente != "sair":
        peso_paciente = float(input("Informe seu peso: "))
        altura_paciente = float(input("Informe sua altura: "))
        imc = peso_paciente / (altura_paciente ** 2)

        registro = {"nome": nome_paciente, "valor_imc": imc}
        historico_pacientes.append(registro)
    else:
        string_sair = nome_paciente

for historico_paciente in historico_pacientes:
    print(f"Paciente: {historico_paciente['nome']}")