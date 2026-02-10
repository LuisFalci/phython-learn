def obter_classificacao(imc):
    if imc < 18.5:
        return "Peso Normal"
    elif 18.5  <= imc <= 24.9 :
        return "Classificação: Peso normal"
    elif 25 <= imc <= 29.9:
        return "Classificação: Sobrepeso"
    else:
        return "Classificação: Obesidade"

def calcular_imc():
    historico_pacientes = []
    string_sair = ""
    while string_sair != "sair":
        nome_paciente = str(input("Informe seu nome ou digite sair para encerrar o fluxo: "))
        if nome_paciente != "sair":
            peso_paciente = float(input("Informe seu peso: "))
            altura_paciente = float(input("Informe sua altura: "))
            imc = peso_paciente / (altura_paciente ** 2)

            registro = {"nome": nome_paciente, "valor_imc": imc}
            historico_pacientes.append(registro)
        else:
            for historico_paciente in historico_pacientes:
                historico_paciente["classificacao"] = obter_classificacao(historico_paciente["valor_imc"])
            string_sair = nome_paciente
            return historico_pacientes
        
def exibir_relatorio(lista_pacientes):
    print(lista_pacientes)

exibir_relatorio(calcular_imc())