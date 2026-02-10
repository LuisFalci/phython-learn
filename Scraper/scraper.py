import requests
from bs4 import BeautifulSoup
import json

url = "https://www.pciconcursos.com.br/concursos/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Lista que armazenará todos os concursos para o JSON
lista_concursos = []
uf_atual = "Não informada"

# busca todas as divs com a classe especificada 
elementos = soup.find_all('div', class_=['ua', 'na', 'ea', 'da'])

# itera todos os elementos capturados acima
for elem in elementos:
    classes = elem.get('class', [])

    # a div com o estado do concurso, fica fora da div com as informações. Assim, precisamos rodar sequencialmente para descobrir o estado.
    if 'ua' in classes:
        uf_div = elem.find('div', class_='uf')
        if uf_div:
            uf_atual = uf_div.text.strip()
            
    elif any(c in classes for c in ['na', 'ea', 'da']):
        ca_div = elem.find('div', class_='ca')
        link_tag = ca_div.find('a') if ca_div else None
        
        link = link_tag['href'] if link_tag and link_tag.has_attr('href') else "Sem link"
        titulo = link_tag.text.strip() if link_tag else "Sem título"
        
        detalhes_div = elem.find('div', class_='cd')
        detalhes = detalhes_div.get_text(separator=" ").strip() if detalhes_div else "Sem detalhes"
        
        # Criamos um dicionário com os dados capturados
        dados = {
            "uf": uf_atual,
            "status": classes[0].upper(),
            "titulo": titulo,
            "link": link,
            "detalhes": detalhes
        }
        
        # Adicionamos o dicionário à nossa lista
        lista_concursos.append(dados)

# --- SALVANDO O ARQUIVO JSON ---
nome_arquivo = "concursos.json"

with open(nome_arquivo, 'w', encoding='utf-8') as f:
    # indent=4 deixa o arquivo legível para humanos
    # ensure_ascii=False garante que acentos fiquem corretos
    json.dump(lista_concursos, f, indent=4, ensure_ascii=False)

print(f"Sucesso! {len(lista_concursos)} concursos salvos em {nome_arquivo}")