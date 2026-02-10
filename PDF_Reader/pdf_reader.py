import fitz
import os

def extrair_pdf(local):
    documento = fitz.open(local)
    texto_completo = ""
    
    # Corrigido: Fechamos o parênteses do range
    for numero_pagina in range(len(documento)):
        # Corrigido: documento (com 't')
        pagina = documento.load_page(numero_pagina)
        texto_completo += pagina.get_text()
        
    documento.close()
    return texto_completo

# Dinâmico: Pega a pasta onde este script .py está salvo
pasta_raiz = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_raiz, "Mesopotamia.pdf")

# Chamando a função com o caminho correto
try:
    resultado = extrair_pdf(caminho_arquivo)
    print(resultado)
except Exception as e:
    print(f"Erro ao abrir o arquivo: {e}")