import requests
from bs4 import BeautifulSoup
import json
import os
import schedule
import time

def executar_scraper():
    url = "https://www.pciconcursos.com.br/concursos/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    nome_arquivo = "concursos.json"
    
    # 1. Carregar dados existentes para evitar duplicatas
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            lista_concursos = json.load(f)
    else:
        lista_concursos = []

    # Criamos um set de links já salvos para busca rápida
    links_existentes = {c['link'] for c in lista_concursos}
    novos_concursos_contagem = 0

    uf_atual = "Não informada"
    elementos = soup.find_all('div', class_=['ua', 'na', 'ea', 'da'])

    for elem in elementos:
        classes = elem.get('class', [])

        if 'ua' in classes:
            uf_div = elem.find('div', class_='uf')
            if uf_div:
                uf_atual = uf_div.text.strip()
                
        elif any(c in classes for c in ['na', 'ea', 'da']):
            ca_div = elem.find('div', class_='ca')
            link_tag = ca_div.find('a') if ca_div else None
            link = link_tag['href'] if link_tag and link_tag.has_attr('href') else "Sem link"
            
            # --- LÓGICA DE VERIFICAÇÃO ---
            if link in links_existentes or link == "Sem link":
                continue  # Pula se já existir ou se for inválido

            titulo = link_tag.text.strip() if link_tag else "Sem título"
            detalhes_div = elem.find('div', class_='cd')
            detalhes = detalhes_div.get_text(separator=" ").strip() if detalhes_div else "Sem detalhes"
            data_inscricao = elem.find('div', class_='ce')
            data = data_inscricao.get_text(separator=" ").strip() if data_inscricao else "Sem detalhes"

            dados = {
                "uf": uf_atual,
                "status": classes[0].upper(),
                "titulo": titulo,
                "link": link,
                "data": data,
                "detalhes": detalhes
            }
            
            lista_concursos.append(dados)
            links_existentes.add(link)
            novos_concursos_contagem += 1

    # 2. Salvar apenas se houver novidades
    if novos_concursos_contagem > 0:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(lista_concursos, f, indent=4, ensure_ascii=False)
        print(f"Sucesso! {novos_concursos_contagem} novos concursos adicionados.")
    else:
        print("Nenhuma novidade encontrada.")

if __name__ == "__main__":
    executar_scraper()
    
# Agendar para cada 1 hora
schedule.every(1).hours.do(executar_scraper)

print("Scraper ativo. Pressione Ctrl+C para parar.")
while True:
    schedule.run_pending()
    time.sleep(1)