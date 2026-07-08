# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def buscar_marcas():
    url = "https://google.com"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []

    for g in soup.select("div.g"):
        title = g.find("h3")
        link = g.find("a")

        if title and link:
            resultados.append({
                "marca": title.text,
                "web": link["href"]
            })

    return resultados


def main():
    marcas = buscar_marcas()

    print("Leads encontrados:\n")

    for m in marcas[:5]:
        print(m)


if __name__ == "__main__":
    main()
